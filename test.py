import requests

jar = requests.cookies.RequestsCookieJar()
session = requests.Session()
response1 = session.get('https://www.etsy.com', verify=False, cookies=jar)  # or post ...
jar.update(response1.cookies)
cookies = requests.utils.dict_from_cookiejar(jar)
print(response1.headers)