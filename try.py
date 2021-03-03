# import csv
# import re
# with open('innob.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         # print(row[1].type())
#         res = re.findall(
#             r’(?<=\.)([ ^ .]+)(?: \.(?: co\.uk|ac\.us|[^.]+(?: $|\n)))’, row[1])
#         print(res)

# import requests
# try:
#     scrapedhtml = requests.get(
#         "https://www.google.com/search?q=nike+shoes.", timeout=0.075).text
# except requests.Timeout as e:
#     print("OOPS!! Timeout Error")
#     scrapedhtml = "Oops Timeout Error"
# finally:
#     record_file = open('htmlfile.html', 'w')
#     record_file.write(scrapedhtml)
#     record_file.close()

# import requests
# from bs4 import BeautifulSoup
# source = requests.get(
#     "https://covid19.who.int/region/searo/country/np").text
# soup = BeautifulSoup(source, 'lxml')
# div_element = soup.find('div', id="___gatsby")
# finddiv = div_element.find('div', class_="sc-AxjAm sc-AxiKw igEipw")
# print(finddiv.p.text)

import requests
from bs4 import BeautifulSoup
source = requests.get(
    "https://covid19.who.int/table").text
soup = BeautifulSoup(source, 'lxml')
div_element = soup.find('div', id="gatsby-focus-wrapper")
finddiv = div_element.find('div', class_="sc-pktCe dSKYub")

record_file = open('coronafile.html', 'w')
record_file.write(soup.prettify())
record_file.close()
