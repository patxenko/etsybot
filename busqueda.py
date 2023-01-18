import requests
from bs4 import BeautifulSoup
import curlfunc as curlfunc


def request_item(url):
    response = requests.get(url)
    return response


def lazy_second_load(listing_ids, ad_ids, logging_keys):
    cookies = curlfunc.get_cookie()
    headers = curlfunc.get_headers()
    data = {
        'log_performance_metrics': 'true',
        'specs[listingCards][]': 'Search2_ApiSpecs_LazyListingCards',
        'specs[listingCards][1][listing_ids][]': listing_ids,
        'specs[listingCards][1][ad_ids][]': ad_ids,
        'specs[listingCards][1][logging_keys][]': logging_keys,
        'specs[listingCards][1][search_request_params][detected_locale][language]': 'es',
        'specs[listingCards][1][search_request_params][detected_locale][currency_code]': 'EUR',
        'specs[listingCards][1][search_request_params][detected_locale][region]': 'ES',
        'specs[listingCards][1][search_request_params][locale][language]': 'es',
        'specs[listingCards][1][search_request_params][locale][currency_code]': 'EUR',
        'specs[listingCards][1][search_request_params][locale][region]': 'ES',
        'specs[listingCards][1][search_request_params][name_map][query]': 'q',
        'specs[listingCards][1][search_request_params][name_map][query_type]': 'qt',
        'specs[listingCards][1][search_request_params][name_map][results_per_page]': 'result_count',
        'specs[listingCards][1][search_request_params][name_map][min_price]': 'min',
        'specs[listingCards][1][search_request_params][name_map][max_price]': 'max',
        'specs[listingCards][1][search_request_params][parameters][q]': 'pendientes plata',
        'specs[listingCards][1][search_request_params][parameters][ref]': 'auto-1',
        'specs[listingCards][1][search_request_params][parameters][page]': '1',
        'specs[listingCards][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/es/search?q=pendientes+plata&ref=auto-1&as_prefix=encuentra+nombres+de+tiendas+que+contengan+pendientes',
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
        'specs[listingCards][1][search_request_params][parameters][eligibility_map][language]': 'es',
        'specs[listingCards][1][search_request_params][parameters][eligibility_map][last_login]': '',
        'specs[listingCards][1][search_request_params][parameters][eligibility_map][purchases_awaiting_review]': '',
        'specs[listingCards][1][search_request_params][parameters][eligibility_map][push_notification_settings]': '',
        'specs[listingCards][1][search_request_params][parameters][eligibility_map][region]': 'ES',
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
        'specs[listingCards][1][organic_listings_count]': '1588337',
        'view_data_event_name': 'search_lazy_loaded_cards_specview_rendered',
    }
    response = requests.post(
        'https://www.etsy.com/api/v3/ajax/bespoke/member/neu/specs/listingCards',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    jsondata = response.json()
    if 'output' in jsondata:
        if 'listingCards' in jsondata['output']:
            html_text = jsondata['output']['listingCards']
        else:
            exit('Datos no encontrados')
    else:
        exit('Datos no encontrados en busqueda')

    contador = 0
    soup = BeautifulSoup(html_text, 'html.parser')
    for link in soup.find_all('a'):
        title = link.get('title')
        enlace = link.get('href')
        if (title is not None and enlace is not None):
            contador = contador + 1
            print(title + ": " + enlace)
            item_resp = request_item(enlace)

            itemsoup = BeautifulSoup(item_resp.text, 'html.parser')
            for span in itemsoup.find_all("span", {"class": "wt-badge wt-badge--status-02 wt-ml-xs-2"}):
                print(str(span.contents[0].strip()))

    print("Articulos2: " + str(contador))
