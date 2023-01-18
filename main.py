import requests
import json
from bs4 import BeautifulSoup
import time
import curlfunc as curlfunc
import busqueda as busqueda

inicio = time.time()


cookies = curlfunc.get_cookie()
headers = curlfunc.get_headers()

data = {
    'log_performance_metrics': 'true',
    'specs[async_search_results][]': 'Search2_ApiSpecs_WebSearch',
    'specs[async_search_results][1][search_request_params][detected_locale][language]': 'es',
    'specs[async_search_results][1][search_request_params][detected_locale][currency_code]': 'EUR',
    'specs[async_search_results][1][search_request_params][detected_locale][region]': 'ES',
    'specs[async_search_results][1][search_request_params][locale][language]': 'es',
    'specs[async_search_results][1][search_request_params][locale][currency_code]': 'EUR',
    'specs[async_search_results][1][search_request_params][locale][region]': 'ES',
    'specs[async_search_results][1][search_request_params][name_map][query]': 'q',
    'specs[async_search_results][1][search_request_params][name_map][query_type]': 'qt',
    'specs[async_search_results][1][search_request_params][name_map][results_per_page]': 'result_count',
    'specs[async_search_results][1][search_request_params][name_map][min_price]': 'min',
    'specs[async_search_results][1][search_request_params][name_map][max_price]': 'max',
    'specs[async_search_results][1][search_request_params][parameters][q]': 'pendientes plata',
    'specs[async_search_results][1][search_request_params][parameters][ref]': 'auto-1',
    'specs[async_search_results][1][search_request_params][parameters][as_prefix]': 'encuentra nombres de tiendas que contengan pendientes',
    'specs[async_search_results][1][search_request_params][parameters][page]': '1',
    'specs[async_search_results][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/es/search?q=pendientes%20de%20oro&ref=auto-1&as_prefix=pendientes%20de%20oro',
    'specs[async_search_results][1][search_request_params][parameters][is_prefetch]': 'false',
    'specs[async_search_results][1][search_request_params][parameters][placement]': 'wsg',
    'specs[async_search_results][1][search_request_params][user_id]': '',
    'specs[async_search_results][1][request_type]': 'reformulation',
    'view_data_event_name': 'search_async_reformulation_specview_rendered',
}

response = requests.post(
    'https://www.etsy.com/api/v3/ajax/bespoke/member/neu/specs/async_search_results',
    cookies=cookies,
    headers=headers,
    data=data,
)

def request_item (url):
    response = requests.get(url)
    return response

jsondata = response.json()

# OBTENEMOS LOS LAZY LOADED LISTING IDS Y LOS LAZY LOADED AD IDS y lazy_loaded_logging_keys
if 'jsData' in jsondata:
    if 'lazy_loaded_listing_ids' in jsondata['jsData']:
        listing_ids = jsondata['jsData']['lazy_loaded_listing_ids']
    else:
        exit('Datos no encontrados de lazy_loaded_listing_ids')
    if 'lazy_loaded_logging_keys' in jsondata['jsData']:
        logging_keys = jsondata['jsData']['lazy_loaded_logging_keys']
    else:
        exit('Datos no encontrados de lazy_loaded_logging_keys')
    if 'lazy_loaded_ad_ids' in jsondata['jsData']:
        ad_ids = jsondata['jsData']['lazy_loaded_ad_ids']
    else:
        exit('Datos no encontrados de lazy_loaded_ad_ids')
else:
    exit('Datos no encontrados')


# OBTENEMOS LOS DATOS DE LOS 12 PRIMEROS PRODUCTOS QUE YA VIENEN AQUI
if 'output' in jsondata:
    if 'async_search_results' in jsondata['output']:
        html_text = jsondata['output']['async_search_results']
    else:
        exit('Datos no encontrados')
else:
    exit('Datos no encontrados')

contador = 0
soup = BeautifulSoup(html_text, 'html.parser')
for link in soup.find_all('a'):
    title = link.get('title')
    enlace = link.get('href')
    if (title is not None and enlace is not None):
        contador=contador+1
        print(title + ": " + enlace)
        item_resp = request_item(enlace)

        itemsoup = BeautifulSoup(item_resp.text, 'html.parser')
        for span in itemsoup.find_all("span", {"class": "wt-badge wt-badge--status-02 wt-ml-xs-2"}):
            print(str(span.contents[0].strip()))

print("Articulos1: " + str(contador))
#Hacemos la segunda peticion de busqueda:
busqueda.lazy_second_load(listing_ids, ad_ids, logging_keys)

fin = time.time()
print(fin-inicio) # 1.0005340576171875
