import requests
with requests.Session() as s:
    url = 'https://myaccount.keralavisionisp.com/Customer/Default.aspx'
    r = s.get(url)
    print(r.content)
