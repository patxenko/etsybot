from concurrent.futures import ThreadPoolExecutor
import time
import requests
from bs4 import BeautifulSoup
import reviews as reviews

def hilillo_request(url):
    item_resp = requests.get(url, verify=False)
    itemsoup = BeautifulSoup(item_resp.text, 'html.parser')

    if len(itemsoup.find_all("span", {"class": "wt-badge wt-badge--status-02 wt-ml-xs-2"})) > 0:
        # print("Entramos a por reviews de " + str(enlace))
        rev = reviews.reviews(data_shop_id, data_listing_id, self.cookies, self.headers)
        reviews_totales = rev.get_reviews_que_cumple()
        reviews_totales_quince = rev.contador_reviews_quince
    else:
        reviews_totales = 0
        reviews_totales_quince = 0
    dictio = {'title': title, 'url': enlace, 'last15': reviews_totales_quince,
              'last30': reviews_totales}
    self.primera_tanda.append(dictio)


dictio = {'title': title, 'url': enlace, 'last15': reviews_totales_quince,
                                  'last30': reviews_totales}
list_links = ['https://www.etsy.com/listing/1293684089/argentina-world-champion-who-looks-silly',
              'https://www.etsy.com/listing/1149992809/cute-fat-belly-mug-coffee-mug-handmade',
              'https://www.etsy.com/listing/1235991522/coffee-mug-japanese-hand-crafted',
              'https://www.etsy.com/listing/893596842/pottery-mug-handmade-ceramic-mug-coffee']

res = []
with ThreadPoolExecutor(max_workers=4) as executor:
    for link in list_links:
        future = executor.submit(hilillo_request, link)
res.append(future.result())  # Here
print(res)