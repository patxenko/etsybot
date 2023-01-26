import requests
from bs4 import BeautifulSoup
import datetime

requests.packages.urllib3.disable_warnings()


class reviews:
    def __init__(self, data_shop_id, data_listing_id, cookies, headers):
        self.data_shop_id = data_shop_id
        self.data_listing_id = data_listing_id
        self.pagina_reviews = 1
        self.list_months = {'ene': 1, 'feb': 2, 'mar': 3, 'abr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'ago': 8, 'sep': 9,
                            'oct': 10,
                            'nov': 11, 'dic': 12}
        self.list_months2 = {
            'jan': 1,
            'feb': 2,
            'mar': 3,
            'apr': 4,
            'may': 5,
            'jun': 6,
            'jul': 7,
            'aug': 8,
            'sep': 9,
            'oct': 10,
            'nov': 11,
            'dec': 12
        }

        ahora = datetime.datetime.utcnow()
        self.haceunmes = ahora - datetime.timedelta(days=31)
        self.hacequince = ahora - datetime.timedelta(days=15)
        self.contador_reviews = 0
        self.contador_reviews_quince = 0
        self.cookies = cookies
        self.headers = headers

    def get_reviews(self):
        data = {
            'log_performance_metrics': 'false',
            'specs[reviews][]': 'Etsy\\Modules\\ListingPage\\Reviews\\ApiSpec',
            'specs[reviews][1][listing_id]': self.data_listing_id,
            'specs[reviews][1][shop_id]': self.data_shop_id,
            'specs[reviews][1][render_complete]': 'true',
            'specs[reviews][1][active_tab]': 'same_listing_reviews',
            'specs[reviews][1][should_lazy_load_images]': 'false',
            'specs[reviews][1][should_use_pagination]': 'false',
            'specs[reviews][1][page]': self.pagina_reviews,
            'specs[reviews][1][should_show_variations]': 'false',
            'specs[reviews][1][is_reviews_untabbed_cached]': 'false',
            'specs[reviews][1][was_landing_from_external_referrer]': 'false',
            'specs[reviews][1][filter_has_photos]': 'false',
            'specs[reviews][1][filter_rating]': '0',
            'specs[reviews][1][sort_option]': 'Recency',
        }
        response_reviews = requests.post(
            'https://www.etsy.com/api/v3/ajax/bespoke/member/neu/specs/reviews',
            cookies=self.cookies,
            headers=self.headers,
            data=data,
            verify=False
        )
        jsondata_reviews = response_reviews.json()
        if 'output' in jsondata_reviews:
            if 'reviews' in jsondata_reviews['output']:
                html_text_reviews = jsondata_reviews['output']['reviews']
            else:
                exit('Reviews no encontrados')
        else:
            print(
                str(jsondata_reviews) + " para listing" + str(self.data_listing_id) + " shop " + str(self.data_shop_id))
            exit('Datos no encontrados en output reviews')
        soup_r = BeautifulSoup(html_text_reviews, 'html.parser')
        if len(soup_r.find_all('p', class_='wt-text-caption wt-text-gray')) == 0:
            return 0
        for fechita in soup_r.find_all('p', class_='wt-text-caption wt-text-gray'):
            fech = (fechita.get_text().strip()).split()
            anyo = fech[len(fech) - 1]
            mes = fech[len(fech) - 3].replace(",", '').lower()
            dia = fech[len(fech) - 2].replace(",", '')
            # print("El resultado es este: " + str(fech))
            if anyo.isnumeric() is False or dia.isnumeric() is False:
                continue
            fechaRecogida = datetime.datetime(int(anyo), int(self.list_months2[mes]), int(dia))
            # print("La fecha recogida es " + str(fechaRecogida))
            if fechaRecogida > self.hacequince:
                self.contador_reviews_quince = self.contador_reviews_quince + 1
            if fechaRecogida > self.haceunmes:
                self.contador_reviews = self.contador_reviews + 1
            else:
                return 0
        if len(soup_r.find_all('p', class_='wt-text-caption wt-text-gray')) == 0:
            return 0
        return 1

    def pasa_pagina(self):
        self.pagina_reviews = self.pagina_reviews + 1

    def get_reviews_que_cumple(self):
        res = 1
        while res == 1:
            res = self.get_reviews()
            if res == 0:
                break
            self.pasa_pagina()
        print("- Reviews totales: " + str(self.contador_reviews))
        return self.contador_reviews
