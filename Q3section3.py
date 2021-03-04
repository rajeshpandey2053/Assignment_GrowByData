import requests
url = "https://covid19.who.int/page-data/index/page-data.json"
proxies = {}
response = requests.get(url=url, proxies=proxies)
with open("response.csv", 'wb') as f:
    f.write(response.content)
