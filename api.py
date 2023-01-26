import requests
requests.packages.urllib3.disable_warnings()

r = requests.get('https://openapi.etsy.com/v3/application/buyer-taxonomy/nodes?api_key=099jw6me58dzl5jdtqsdzt6b',verify=False)
print(r)

header = {'x-api-key': '099jw6me58dzl5jdtqsdzt6b'}

response = requests.get('https://openapi.etsy.com/v3/application/buyer-taxonomy/nodes', headers=header, verify=False)


if response.status_code == 401:
    exit('Unauthorized')


