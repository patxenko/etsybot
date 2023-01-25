import requests
from bs4 import BeautifulSoup


def get_cookie():
    complete()
    exit()
    response = requests.get('https://www.etsy.com/', verify=False)
    cookies = response.cookies
    for cookie in cookies:
        print(cookie)
    exit()
    cookies_jar = requests.cookies.RequestsCookieJar()
    print(cookies_jar)
    exit()
    return cookies_jar

    cookies2 = {
        'uaid': 'vP9eQESfBtTB4TEpXfRGqBgOE_hjZACC5CPmP2F0tVJpYmaKkpWSR1FFemRweWRkoqFftoV7RWlBfkB8Vl5VVk6xr1ItAwA.',
        'fve': '1673803769.0',
        'ua': '531227642bc86f3b5fd7103a0c0b4fd6',
        'p': 'eyJnZHByX3RwIjoxLCJnZHByX3AiOjF9',
        '_gcl_au': '1.1.1262324430.1673803864',
        '_gid': 'GA1.2.1532402406.1673803864',
        '_pin_unauth': 'dWlkPVpEVXlNMlpsWkRjdE9UZG1NUzAwTVRnekxXRTJOMlF0TldOaU56VXlNbUl6TWpOaA',
        '__adal_ca': 'so%3Ddirect%26me%3Dnone%26ca%3Ddirect%26co%3D%28not%2520set%29%26ke%3D%28not%2520set%29',
        '__adal_cw': '1673803916366',
        'granify.new_user.QrsCf': 'true',
        'granify.uuid': '97101238-c9ae-46f6-8cd8-336f110d4e31',
        'granify.session.QrsCf': '-1',
        'user_prefs': 'ixT1cCd9yYAs7BVym1cz7hgUI7hjZACC5CPmPyG05adoJdfQICWdvNKcHB2l1GIlHSXXYCjXCELhImIZAA..',
        '__adal_id': '0e3a9645-aafd-41a3-a9f6-6a327204f3ae.1673803916.1.1673804276.1673803916.3ac78bec-57d8-495f-ab05-68ea40ab61a0',
        '_tq_id.TV-27270909-1.a4d5': '5d25f7b48298d68c.1673803917.0.1673804276..',
        'last_browse_page': 'https%3A%2F%2Fwww.etsy.com%2F',
        '_ga_KR3J610VYM': 'GS1.1.1673879768.4.1.1673879899.60.0.0',
        'pla_spr': '0',
        '_ga': 'GA1.1.1547202360.1673803864',
        '_uetsid': '62c4c38094fa11edbdffed4abb1b1a72',
        '_uetvid': '74efbef07b1311eda2976910e1322adb',
        'tsd': '%7B%22gnav_search_focus%22%3A%7B%22event_name%22%3A%22gnav_search_focus%22%2C%22interaction_type%22%3A%22click%22%7D%7D',
        'search_options': '{"prev_search_term":null,"item_language":null,"language_carousel":null}',
    }
    return cookies


def get_headers():
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
        'x-csrf-token': '3:1673879898:GjVFHjEzmpCro9ThkH3Gl4ChYaJM:5a52b41a95af5ab37ae843c6cda77cb8000b253ef5688d43d17cc462b8787ea1',
        'x-page-guid': 'f394e2af277.5dc8ddb1c03db037b281.00',
        'x-recs-primary-location': 'https://www.etsy.com/',
        'x-recs-primary-referrer': 'https://www.etsy.com/',
        'x-requested-with': 'XMLHttpRequest',
    }
    return headers


def complete():
    jar = requests.cookies.RequestsCookieJar()
    session = requests.Session()
    response1 = session.get('https://www.etsy.com', verify=False, cookies=jar)  # or post ...
    jar.update(response1.cookies)

    cookies = requests.utils.dict_from_cookiejar(jar)
    headers = session.headers
    print(cookies)
    print(headers)
    soup = BeautifulSoup(response1.text, 'html.parser')
    # parseamos la respuesta para coger el nonce




    # cookies['ua'] = '531227642bc86f3b5fd7103a0c0b4fd6'
    # cookies['p'] = 'eyJnZHByX3RwIjoxLCJnZHByX3AiOjF9'
    # cookies['fve'] = '1673803769.0'
    # cookies['uaid']='vP9eQESfBtTB4TEpXfRGqBgOE_hjZACC5CPmP2F0tVJpYmaKkpWSR1FFemRweWRkoqFftoV7RWlBfkB8Vl5VVk6xr1ItAwA.'


    data = {
        'log_performance_metrics': 'true',
        'specs[async_search_results][]': 'Search2_ApiSpecs_WebSearch',
        'specs[async_search_results][1][search_request_params][detected_locale][language]': '',
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
        'specs[async_search_results][1][search_request_params][parameters][q]': 'pulseras',
        'specs[async_search_results][1][search_request_params][parameters][ref]': 'pagination',
        'specs[async_search_results][1][search_request_params][parameters][as_prefix]': '',
        'specs[async_search_results][1][search_request_params][parameters][page]': 1,
        'specs[async_search_results][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/es/search?q=pulseras',
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
        verify=False
    )
    jsondata = response.json()
    print(jsondata)
    exit()
