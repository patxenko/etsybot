import requests
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()


def get_headers(token):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.etsy.com',
        'Referer': 'https://www.etsy.com/search?q=cosas+nuevas',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'X-Page-GUID': 'f3b1fa0b12d.97a359182b31b5d84f19.00',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'x-csrf-token': token,
        'x-detected-locale': 'EUR|en-US|ES',
        'x-recs-primary-location': 'https://www.etsy.com/search?q=cosas+nuevas',
        'x-recs-primary-referrer': 'https://www.etsy.com/',
    }
    return headers


def get_csrf_token(response1):
    token = False
    soup = BeautifulSoup(response1.text, 'html.parser')
    for res in soup.find_all("meta", {"name": "csrf_nonce"}):
        token = True
        csrf_coken = res['content']
    if token == False:
        exit("No token recovered")
    return csrf_coken


session = requests.Session()
session.cookies.clear()
jar = requests.cookies.RequestsCookieJar()
response1 = session.get('https://www.etsy.com', verify=False, cookies=jar)  # or post ...
jar.update(response1.cookies)
cookies = requests.utils.dict_from_cookiejar(jar)
csrf_token = get_csrf_token(response1)
headers = get_headers(csrf_token)

# cookies = {
#    'uaid': 'UBkKv13emHPLDr3vN74gWlX4wiRjZACC5Itu02F0tVJpYmaKkpVSsJehh0VSlre3X1pEqntGUr5piUeeWZ55YEVGvlItAwA.',
#    'user_prefs': '0zFSLEtu3yN_RX4bKDUFii1TJYxjZACC5Itu02F0tJJraJCSTl5pTo6OUmqebmiwko6SazBUxAhC4SJiGQA.',
#    'fve': '1674659479.0',
#    'last_browse_page': 'https%3A%2F%2Fwww.etsy.com%2F',
#    'ua': '531227642bc86f3b5fd7103a0c0b4fd6',
#    'p': 'eyJnZHByX3RwIjoxLCJnZHByX3AiOjF9',
#    'pla_spr': '0',
#    '_gcl_au': '1.1.68641045.1674660812',
#    '_ga': 'GA1.2.1789194991.1674660813',
#    '_gid': 'GA1.2.1179219547.1674660813',
#    '_uetsid': 'a07898009cc511ed829af15fbf5270b9',
#    '_uetvid': 'a078eea09cc511ed93e61dbcefc65e6a',
#    '_derived_epik': 'dj0yJnU9dk01TjR1YTVnT1dzRmVkWVdnMjlET2tHYndWaUNLbGkmbj1xYWhFVklmTEhQUV94WVdIdEIxNnB3Jm09MSZ0PUFBQUFBR1BSUzgwJnJtPTEmcnQ9QUFBQUFHUFJTODAmc3A9NQ',
#    '_pin_unauth': 'dWlkPU4yUTBPR1psWTJJdE1EaGtOUzAwWlRBMkxUazJOMkl0WlRBNE1EazRNamMzTlRKbQ',
#    '_ga_KR3J610VYM': 'GS1.1.1674660813.1.1.1674660893.60.0.0',
#    'tsd': '%7B%22gnav_search_focus%22%3A%7B%22event_name%22%3A%22gnav_search_focus%22%2C%22interaction_type%22%3A%22keyboard%22%7D%2C%22gnav_perform_search%22%3A%7B%22event_name%22%3A%22gnav_perform_search%22%2C%22interaction_type%22%3A%22click%22%7D%7D',
#    'search_options': '{"prev_search_term":"cosas%20nuevas","item_language":null,"language_carousel":null}',
# }


data = {
    'log_performance_metrics': 'true',
    'specs[async_search_results][]': 'Search2_ApiSpecs_WebSearch',
    'specs[async_search_results][1][search_request_params][detected_locale][language]': 'en-US',
    'specs[async_search_results][1][search_request_params][detected_locale][currency_code]': 'EUR',
    'specs[async_search_results][1][search_request_params][detected_locale][region]': 'ES',
    'specs[async_search_results][1][search_request_params][locale][language]': 'en-US',
    'specs[async_search_results][1][search_request_params][locale][currency_code]': 'EUR',
    'specs[async_search_results][1][search_request_params][locale][region]': 'ES',
    'specs[async_search_results][1][search_request_params][name_map][query]': 'q',
    'specs[async_search_results][1][search_request_params][name_map][query_type]': 'qt',
    'specs[async_search_results][1][search_request_params][name_map][results_per_page]': 'result_count',
    'specs[async_search_results][1][search_request_params][name_map][min_price]': 'min',
    'specs[async_search_results][1][search_request_params][name_map][max_price]': 'max',
    'specs[async_search_results][1][search_request_params][parameters][q]': 'tazas de madera personalizables',
    'specs[async_search_results][1][search_request_params][parameters][page]': '1',
    'specs[async_search_results][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/search?q=tazas+de+madera+personalizables',
    'specs[async_search_results][1][search_request_params][parameters][ref]': '',
    'specs[async_search_results][1][search_request_params][parameters][is_prefetch]': 'false',
    'specs[async_search_results][1][search_request_params][parameters][placement]': 'wsg',
    'specs[async_search_results][1][search_request_params][user_id]': '',
    'specs[async_search_results][1][request_type]': 'reformulation',
    'view_data_event_name': 'search_async_reformulation_specview_rendered',
}

response = requests.post(
    'https://www.etsy.com/api/v3/ajax/bespoke/member/neu/specs/async_search_results?__a=1',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False
)

jsondata = response.json()

# OBTENEMOS LOS LAZY LOADED LISTING IDS Y LOS LAZY LOADED AD IDS y lazy_loaded_logging_keys
if 'jsData' in jsondata:
    if 'lazy_loaded_listing_ids' in jsondata['jsData']:
        listing_ids = jsondata['jsData']['lazy_loaded_listing_ids']
    else:
        print('Datos no encontrados de lazy_loaded_listing_ids')
    if 'lazy_loaded_logging_keys' in jsondata['jsData']:
        logging_keys = jsondata['jsData']['lazy_loaded_logging_keys']
    else:
        print('Datos no encontrados de lazy_loaded_logging_keys')
    if 'lazy_loaded_ad_ids' in jsondata['jsData']:
        ad_ids = jsondata['jsData']['lazy_loaded_ad_ids']
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
contador_productos = 0
deshechados = 0
for div in soup.find_all("li"):
    for li in div.find_all(attrs={"data-page-type": "search"}):
        for link in li.find_all('a'):
            title = link.get('title')
            enlace = link.get('href')
            data_shop_id = li.get('data-shop-id')
            data_listing_id = link.get('data-listing-id')
            if title is not None and enlace is not None:
                if data_listing_id is None or data_shop_id is None:
                    deshechados = deshechados + 1
                    continue
                contador_productos = contador_productos + 1
print(str(contador_productos))
