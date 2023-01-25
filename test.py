import requests
requests.packages.urllib3.disable_warnings()


cookies = {
    'fve': '1673542030.0',
    'ua': '531227642bc86f3b5fd7103a0c0b4fd6',
    'utm_lps': 'google__cpc',
    'p': 'eyJnZHByX3RwIjoxLCJnZHByX3AiOjF9',
    '_gcl_au': '1.1.929557634.1673886849',
    '_pin_unauth': 'dWlkPU5UbGlNMlEzTmprdE5HSmxOeTAwWkdWaExXSm1NekV0WWpZNE1UTm1ZV00yTkRabA',
    '_gcl_aw': 'GCL.1673966840.Cj0KCQiAq5meBhCyARIsAJrtdr6CZexMwAUczG6bIjSujgC2FYs14K948zcVSFj46tZBVYLXbTAnEKEaAo7LEALw_wcB',
    'ken_gclid': 'Cj0KCQiAq5meBhCyARIsAJrtdr6CZexMwAUczG6bIjSujgC2FYs14K948zcVSFj46tZBVYLXbTAnEKEaAo7LEALw_wcB',
    '_gac_UA-2409779-1': '1.1673966840.Cj0KCQiAq5meBhCyARIsAJrtdr6CZexMwAUczG6bIjSujgC2FYs14K948zcVSFj46tZBVYLXbTAnEKEaAo7LEALw_wcB',
    'gift_session_v2': 'pgXtrT_qRn4T4v_f5tm_uxN9qjRjZACC5OM3I2G0IQMA',
    '_tq_id.TV-8172638145-1.a4d5': '4d49881875c0bf75.1674041831.0.1674041835..',
    'granify.new_user.j2TfP': 'true',
    'granify.uuid': 'f2115e4e-254a-4776-9ded-bcf9cac7da1a',
    'granify.session.j2TfP': '-1',
    'user_prefs': '4jEdDtVPrlhrL2UGm1_pFuJ_V4JjZACC5AOWfWD6pPblaCXX0CAlnbzSnBwdpdRiJR0l12Ao1whC4SJiGQA.',
    'uaid': '_76PV1DWYgXQ_EzJmhVG3NQ1gANjZACC5AOWfWD6VPvJaqXSxMwUJSulcveKIEOzYMdgo-TiZCPnPDPv5NwIv_wci1DTQqVaBgA.',
    '_gid': 'GA1.2.1506140130.1674634765',
    'pla_spr': '0',
    'last_browse_page': 'https%3A%2F%2Fwww.etsy.com%2F',
    '_dc_gtm_UA-2409779-1': '1',
    'search_options': '{"prev_search_term":"tazas%20de%20madera%20personalizables","item_language":null,"language_carousel":null}',
    '_ga_KR3J610VYM': 'GS1.1.1674658033.20.1.1674658053.40.0.0',
    '_ga': 'GA1.1.1752925116.1673886850',
    '_uetsid': 'fabe93809c8811ed83b5e332570db258',
    '_uetvid': 'e0e45cf040d311ed88ba8f84e6a6a500',
    '_derived_epik': 'dj0yJnU9N0NJMlZNOFNmc3VTcGQ0eWpIMEkyUTRlYW91TnlQdVImbj1tNGctYVBVZHJZdzNjQTc1UERhN2FnJm09MSZ0PUFBQUFBR1BSUVFVJnJtPTEmcnQ9QUFBQUFHUFJRUVUmc3A9Mg',
    'tsd': '%7B%22gnav_search_focus%22%3A%7B%22event_name%22%3A%22gnav_search_focus%22%2C%22interaction_type%22%3A%22keyboard%22%7D%2C%22gnav_perform_search%22%3A%7B%22event_name%22%3A%22gnav_perform_search%22%2C%22interaction_type%22%3A%22click%22%7D%7D',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'fve=1673542030.0; ua=531227642bc86f3b5fd7103a0c0b4fd6; utm_lps=google__cpc; p=eyJnZHByX3RwIjoxLCJnZHByX3AiOjF9; _gcl_au=1.1.929557634.1673886849; _pin_unauth=dWlkPU5UbGlNMlEzTmprdE5HSmxOeTAwWkdWaExXSm1NekV0WWpZNE1UTm1ZV00yTkRabA; _gcl_aw=GCL.1673966840.Cj0KCQiAq5meBhCyARIsAJrtdr6CZexMwAUczG6bIjSujgC2FYs14K948zcVSFj46tZBVYLXbTAnEKEaAo7LEALw_wcB; ken_gclid=Cj0KCQiAq5meBhCyARIsAJrtdr6CZexMwAUczG6bIjSujgC2FYs14K948zcVSFj46tZBVYLXbTAnEKEaAo7LEALw_wcB; _gac_UA-2409779-1=1.1673966840.Cj0KCQiAq5meBhCyARIsAJrtdr6CZexMwAUczG6bIjSujgC2FYs14K948zcVSFj46tZBVYLXbTAnEKEaAo7LEALw_wcB; gift_session_v2=pgXtrT_qRn4T4v_f5tm_uxN9qjRjZACC5OM3I2G0IQMA; _tq_id.TV-8172638145-1.a4d5=4d49881875c0bf75.1674041831.0.1674041835..; granify.new_user.j2TfP=true; granify.uuid=f2115e4e-254a-4776-9ded-bcf9cac7da1a; granify.session.j2TfP=-1; user_prefs=4jEdDtVPrlhrL2UGm1_pFuJ_V4JjZACC5AOWfWD6pPblaCXX0CAlnbzSnBwdpdRiJR0l12Ao1whC4SJiGQA.; uaid=_76PV1DWYgXQ_EzJmhVG3NQ1gANjZACC5AOWfWD6VPvJaqXSxMwUJSulcveKIEOzYMdgo-TiZCPnPDPv5NwIv_wci1DTQqVaBgA.; _gid=GA1.2.1506140130.1674634765; pla_spr=0; last_browse_page=https%3A%2F%2Fwww.etsy.com%2F; _dc_gtm_UA-2409779-1=1; search_options={"prev_search_term":"tazas%20de%20madera%20personalizables","item_language":null,"language_carousel":null}; _ga_KR3J610VYM=GS1.1.1674658033.20.1.1674658053.40.0.0; _ga=GA1.1.1752925116.1673886850; _uetsid=fabe93809c8811ed83b5e332570db258; _uetvid=e0e45cf040d311ed88ba8f84e6a6a500; _derived_epik=dj0yJnU9N0NJMlZNOFNmc3VTcGQ0eWpIMEkyUTRlYW91TnlQdVImbj1tNGctYVBVZHJZdzNjQTc1UERhN2FnJm09MSZ0PUFBQUFBR1BSUVFVJnJtPTEmcnQ9QUFBQUFHUFJRUVUmc3A9Mg; tsd=%7B%22gnav_search_focus%22%3A%7B%22event_name%22%3A%22gnav_search_focus%22%2C%22interaction_type%22%3A%22keyboard%22%7D%2C%22gnav_perform_search%22%3A%7B%22event_name%22%3A%22gnav_perform_search%22%2C%22interaction_type%22%3A%22click%22%7D%7D',
    'Origin': 'https://www.etsy.com',
    'Referer': 'https://www.etsy.com/es/search?q=tazas+de+madera+personalizable',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'X-Page-GUID': 'f3b1dfb215b.0c5e0099c257073487f4.00',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-csrf-token': '3:1674658048:nrlKCvZ04pvet9ts9TUNfuNOdbza:d6db55cc6894eef731d7f376c1a8d9e1444d8fb983f4bbab34ada7cd403de4ae',
    'x-detected-locale': 'EUR|es|ES',
    'x-recs-primary-location': 'https://www.etsy.com/es/search?q=tazas+de+madera+personalizable',
    'x-recs-primary-referrer': 'https://www.etsy.com/',
}

data = {
    'log_performance_metrics': 'true',
    'specs[async_search_results][]': 'Search2_ApiSpecs_WebSearch',
    'specs[async_search_results][1][search_request_params][detected_locale][language]': 'en-US',
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
    'specs[async_search_results][1][search_request_params][parameters][q]': 'tazas de madera personalizable',
    'specs[async_search_results][1][search_request_params][parameter][page]': '1',
    'specs[async_search_results][1][search_request_params][parameters][referrer]': 'https://www.etsy.com/es/search?q=tazas%20de%20madera%20personalizables',
    'specs[async_search_results][1][search_request_params][parameters][ref]': '',
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

print(response.text)
