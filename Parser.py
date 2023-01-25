import requests
from bs4 import BeautifulSoup
import reviews as reviews
import openpyxl
import Copy_excel as ce
from datetime import datetime

requests.packages.urllib3.disable_warnings()


class Parser:
    def __init__(self, keyword, country_iso_code):
        self.jar = requests.cookies.RequestsCookieJar()
        self.session = requests.Session()
        response1 = self.session.get('https://www.etsy.com', verify=False, cookies=self.jar)  # or post ...
        self.jar.update(response1.cookies)
        self.cookies = requests.utils.dict_from_cookiejar(self.jar)
        self.csrf_token = self.get_csrf_token(response1)

        self.deshechados = 0
        self.listing_ids = []
        self.logging_keys = []
        self.ad_ids = []
        self.contador_productos = 0
        self.headers = self.get_headers()
        self.pagina = 1
        self.keyword = keyword
        self.country_iso_code = country_iso_code
        self.dbname = self.create_db_name()

        # Primero creamos el fichero
        self.excel_name = self.dbname + datetime.now().strftime("%Y_%m_%d") + '.xlsx'
        print("The file is : "+'\033[92m'+str(self.excel_name) + '\033[39m')
        wb = openpyxl.Workbook()
        ws = wb.active
        mylist = ['titulo del producto', 'URL', 'nº reviews past 15 days', 'nº reviews past 30 days']
        ws.append(mylist)
        wb.save(self.excel_name)
        self.row_number = 0
        self.excel = ce.Copy_excel(self.excel_name, self.excel_name)

    def get_csrf_token(self, response1):
        token = False
        soup = BeautifulSoup(response1.text, 'html.parser')
        for res in soup.find_all("meta", {"name": "csrf_nonce"}):
            token = True
            csrf_coken = res['content']
        if token == False:
            exit("No token recovered")
        return csrf_coken

    def create_db_name(self):
        name_ini = self.keyword.replace(" ", "_") + "_" + self.country_iso_code
        return name_ini

    def get_headers(self):
        headers = {
            'authority': 'www.etsy.com',
            'accept': '*/*',
            'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.etsy.com',
            'referer': 'https://www.etsy.com',
            'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
            'x-csrf-token': self.csrf_token,
            'x-recs-primary-location': 'https://www.etsy.com/',
            'x-recs-primary-referrer': 'https://www.etsy.com/',
            'x-requested-with': 'XMLHttpRequest',
        }
        return headers

    def insert_db_data(self, a_insertar):
        for a in a_insertar:
            try:
                if '?' in a['url']:
                    url = a['url'].split('?')[0]
                task = (a['title'], url, a['last15'], a['last30'])
                self.excel.ws.append(task)
                self.excel.save_excel()
            except Exception as e:
                exit(e)

    def request_item(self, url):
        response = self.session.get(url, verify=False)
        return response

    def pasar_pagina(self):
        self.pagina = self.pagina + 1

    def primera_peticion(self):
        print("Primera peticion para la pagina " + str(self.pagina))
        a_insertar = []
        self.listing_ids = []
        self.logging_keys = []
        self.ad_ids = []
        data = {
            'log_performance_metrics': 'true',
            'specs[async_search_results][]': 'Search2_ApiSpecs_WebSearch',
            'specs[async_search_results][1][search_request_params][detected_locale][language]': '',
            'specs[async_search_results][1][search_request_params][detected_locale][currency_code]': 'EUR',
            'specs[async_search_results][1][search_request_params][detected_locale][region]': self.country_iso_code,
            'specs[async_search_results][1][search_request_params][locale][language]': '',
            'specs[async_search_results][1][search_request_params][locale][currency_code]': 'EUR',
            'specs[async_search_results][1][search_request_params][locale][region]': self.country_iso_code,
            'specs[async_search_results][1][search_request_params][name_map][query]': 'q',
            'specs[async_search_results][1][search_request_params][name_map][query_type]': 'qt',
            'specs[async_search_results][1][search_request_params][name_map][results_per_page]': 'result_count',
            'specs[async_search_results][1][search_request_params][name_map][min_price]': 'min',
            'specs[async_search_results][1][search_request_params][name_map][max_price]': 'max',
            'specs[async_search_results][1][search_request_params][parameters][q]': self.keyword,
            'specs[async_search_results][1][search_request_params][parameters][ref]': 'pagination',
            'specs[async_search_results][1][search_request_params][parameters][as_prefix]': '',
            'specs[async_search_results][1][search_request_params][parameters][page]': self.pagina,
            'specs[async_search_results][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/search?q=' + self.keyword,
            'specs[async_search_results][1][search_request_params][parameters][is_prefetch]': 'false',
            'specs[async_search_results][1][search_request_params][parameters][placement]': 'wsg',
            'specs[async_search_results][1][search_request_params][user_id]': '',
            'specs[async_search_results][1][request_type]': 'reformulation',
            'view_data_event_name': 'search_async_reformulation_specview_rendered',
        }
        response = self.session.post(
            'https://www.etsy.com/api/v3/ajax/bespoke/member/neu/specs/async_search_results',
            cookies=self.cookies,
            headers=self.headers,
            data=data,
            verify=False
        )
        print(self.cookies)
        print(self.headers)
        self.jar.update(response.cookies)
        self.cookies = requests.utils.dict_from_cookiejar(self.jar)
        jsondata = response.json()

        # OBTENEMOS LOS LAZY LOADED LISTING IDS Y LOS LAZY LOADED AD IDS y lazy_loaded_logging_keys
        if 'jsData' in jsondata:
            if 'lazy_loaded_listing_ids' in jsondata['jsData']:
                self.listing_ids = jsondata['jsData']['lazy_loaded_listing_ids']
            else:
                print('Datos no encontrados de lazy_loaded_listing_ids')
            if 'lazy_loaded_logging_keys' in jsondata['jsData']:
                self.logging_keys = jsondata['jsData']['lazy_loaded_logging_keys']
            else:
                print('Datos no encontrados de lazy_loaded_logging_keys')
            if 'lazy_loaded_ad_ids' in jsondata['jsData']:
                self.ad_ids = jsondata['jsData']['lazy_loaded_ad_ids']
            else:
                print('Datos no encontrados de lazy_loaded_ad_ids')
        else:
            exit('Datos no encontrados en jsondata parser 1')

        # OBTENEMOS LOS DATOS DE LOS 12 PRIMEROS PRODUCTOS QUE YA VIENEN AQUI
        if 'output' in jsondata:
            if 'async_search_results' in jsondata['output']:
                html_text = jsondata['output']['async_search_results']
            else:
                exit('Datos no encontrados async')
        else:
            exit('Datos no encontrados output')

        soup = BeautifulSoup(html_text, 'html.parser')
        for div in soup.find_all("li"):
            for li in div.find_all(attrs={"data-page-type": "search"}):
                for link in li.find_all('a'):
                    title = link.get('title')
                    enlace = link.get('href')
                    data_shop_id = li.get('data-shop-id')
                    data_listing_id = link.get('data-listing-id')
                    if title is not None and enlace is not None:
                        if data_listing_id is None or data_shop_id is None:
                            self.deshechados = self.deshechados + 1
                            continue
                        self.contador_productos = self.contador_productos + 1
                        item_resp = self.request_item(enlace)
                        itemsoup = BeautifulSoup(item_resp.text, 'html.parser')

                        if len(itemsoup.find_all("span", {"class": "wt-badge wt-badge--status-02 wt-ml-xs-2"})) > 0:
                            # print("Entramos a por reviews de " + str(enlace))
                            rev = reviews.reviews(data_shop_id, data_listing_id, self.cookies, self.headers,
                                                  self.session)
                            reviews_totales = rev.get_reviews_que_cumple()
                            reviews_totales_quince = rev.contador_reviews_quince
                        else:
                            reviews_totales = 0
                            reviews_totales_quince = 0
                        dictio = {'title': title, 'url': enlace, 'last15': reviews_totales_quince,
                                  'last30': reviews_totales}
                        a_insertar.append(dictio)
        if len(a_insertar) > 0:
            self.insert_db_data(a_insertar)
        print("Productos:" + str(self.contador_productos) + " en la pagina " + str(self.pagina))
        return response

    def segunda_peticion(self):
        a_insertar = []
        if len(self.listing_ids) == 0:
            print("Listing ids vacio")
            return 0

        data = {
            'log_performance_metrics': 'true',
            'specs[listingCards][]': 'Search2_ApiSpecs_LazyListingCards',
            'specs[listingCards][1][search_request_params][detected_locale][language]': '',
            'specs[listingCards][1][search_request_params][detected_locale][currency_code]': 'EUR',
            'specs[listingCards][1][search_request_params][detected_locale][region]': self.country_iso_code,
            'specs[listingCards][1][search_request_params][locale][language]': '',
            'specs[listingCards][1][search_request_params][locale][currency_code]': 'EUR',
            'specs[listingCards][1][search_request_params][locale][region]': self.country_iso_code,
            'specs[listingCards][1][search_request_params][name_map][query]': self.keyword,
            'specs[listingCards][1][search_request_params][name_map][query_type]': 'qt',
            'specs[listingCards][1][search_request_params][name_map][results_per_page]': 'result_count',
            'specs[listingCards][1][search_request_params][name_map][min_price]': 'min',
            'specs[listingCards][1][search_request_params][name_map][max_price]': 'max',
            'specs[listingCards][1][search_request_params][parameters][q]': self.keyword,
            'specs[listingCards][1][search_request_params][parameters][ref]': 'auto-1',
            'specs[listingCards][1][search_request_params][parameters][page]': self.pagina,
            'specs[listingCards][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/search?q=' + self.keyword + '&ref=auto-1&as_prefix=',
            'specs[listingCards][1][search_request_params][parameters][is_prefetch]': 'false',
            'specs[listingCards][1][search_request_params][parameters][placement]': 'wsg',
            'specs[listingCards][1][search_request_params][parameters][page_type]': 'search',
            'specs[listingCards][1][search_request_params][parameters][bucket_id]': 'HrxgYSwYYa1Nk8GxupoP_jnzjlsM',
            'specs[listingCards][1][search_request_params][parameters][user_id]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][app_os_version]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][app_version]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][currency]': 'EUR',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][device]': '1,0,0,0,0,0,0,0,0,0,0,0,0,0',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][environment]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][favorited]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][first_visit]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][http_referrer]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][language]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][last_login]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][purchases_awaiting_review]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][push_notification_settings]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][region]': self.country_iso_code,
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][region_language_match]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][seller]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][shop_country]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][tier]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][time]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][time_since_last_login]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][time_since_last_purchase]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][user]': '0',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][exclude_groups]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][exclude_users]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][marketplace]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][user_agent]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][user_dataset]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][geoip]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][gdpr]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][email]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][request_restrictions]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][marketing_channel]': '',
            'specs[listingCards][1][search_request_params][parameters][eligibility_map][page_enum]': '',
            'specs[listingCards][1][search_request_params][parameters][filter_distracting_content]': 'true',
            'specs[listingCards][1][search_request_params][parameters][interleaving_option]': '',
            'specs[listingCards][1][search_request_params][parameters][should_pass_user_location_to_thrift]': 'true',
            'specs[listingCards][1][search_request_params][parameters][result_count]': '48',
            'specs[listingCards][1][search_request_params][user_id]': '',
            'specs[listingCards][1][is_mobile]': 'false',
            'specs[listingCards][1][organic_listings_count]': '682295',
            'view_data_event_name': 'search_lazy_loaded_cards_specview_rendered',
        }
        if len(self.listing_ids) > 0:
            data['specs[listingCards][1][listing_ids][]'] = self.listing_ids
        if len(self.ad_ids) > 0:
            data['specs[listingCards][1][ad_ids][]'] = self.ad_ids
        if len(self.logging_keys) > 0:
            data['specs[listingCards][1][logging_keys][]'] = self.logging_keys
        response = requests.post(
            'https://www.etsy.com/api/v3/ajax/bespoke/member/neu/specs/listingCards',
            cookies=self.cookies,
            headers=self.headers,
            data=data,
            verify=False
        )
        self.jar.update(response.cookies)
        self.cookies = requests.utils.dict_from_cookiejar(self.jar)
        jsondata = response.json()
        if 'output' in jsondata:
            if 'listingCards' in jsondata['output']:
                html_text = jsondata['output']['listingCards']
            else:
                exit('Datos no encontrados')
        else:
            exit('Datos no encontrados en busqueda')
        soup = BeautifulSoup(html_text, 'html.parser')

        for div in soup.find_all("li"):
            for li in div.find_all(attrs={"data-page-type": "search"}):
                for link in li.find_all('a'):
                    title = link.get('title')
                    enlace = link.get('href')
                    data_shop_id = li.get('data-shop-id')
                    data_listing_id = link.get('data-listing-id')
                    if title is not None and enlace is not None:
                        if data_listing_id is None or data_shop_id is None:
                            self.deshechados = self.deshechados + 1
                            continue
                        self.contador_productos = self.contador_productos + 1
                        item_resp = self.request_item(enlace)
                        itemsoup = BeautifulSoup(item_resp.text, 'html.parser')
                        if len(itemsoup.find_all("span", {"class": "wt-badge wt-badge--status-02 wt-ml-xs-2"})) > 0:
                            rev = reviews.reviews(data_shop_id, data_listing_id, self.cookies, self.headers,
                                                  self.session)
                            reviews_totales = rev.get_reviews_que_cumple()
                            reviews_totales_quince = rev.contador_reviews_quince
                        else:
                            reviews_totales = 0
                            reviews_totales_quince = 0
                        dictio = {'title': title, 'url': enlace, 'last15': reviews_totales_quince,
                                  'last30': reviews_totales}
                        a_insertar.append(dictio)
        if len(a_insertar) > 0:
            self.insert_db_data(a_insertar)
        print("Articulos2: " + str(self.contador_productos) + " en la pagina " + str(self.pagina))
