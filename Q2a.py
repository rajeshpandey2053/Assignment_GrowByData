import requests
from bs4 import BeautifulSoup
source = requests.get(
    "https://covid19.who.int/region/searo/country/np").text
soup = BeautifulSoup(source, 'lxml')
find_div = soup.find('div', {"class": "sc-AxjAm sc-AxiKw igEipw"})
print(find_div.p.text)
