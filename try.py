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

# import requests
# from bs4 import BeautifulSoup
# source = requests.get(
#     "https://covid19.who.int/table").text
# soup = BeautifulSoup(source, 'lxml')
# div_element = soup.find('div', id="gatsby-focus-wrapper")
# finddiv = div_element.find('div', class_="sc-pktCe dSKYub")

# record_file = open('coronafile.html', 'w')
# record_file.write(soup.prettify())
# record_file.close()

# response = requests.get("https://covid19.who.int/table", timeout=5)
# content = BeautifulSoup(response.content, "html.parser")
# record_file = open('coronafile.html', 'w')
# record_file.write(content.prettify())
# record_file.close()

# import requests
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
# import operator
# import itertools
# # url of the page we want to scrape
# url = "https://covid19.who.int/table"

# # initiating the webdriver. Parameter includes the path of the webdriver.
# driver = webdriver.Chrome('/usr/bin/chromedriver')
# driver.get(url)

# # this is just to ensure that the page is loaded
# time.sleep(5)

# html = driver.page_source

# # this renders the JS code and stores all
# # of the information in static HTML code.

# # Now, we could simply apply bs4 to html variable
# soup = BeautifulSoup(html, "html.parser")
# # finding the container element which has all the rows of cumulative data
# rowgroup_element = soup.find('div', {"role": "rowgroup"})
# # listing all the rows which contains individual cumulative values of each country
# div_row = rowgroup_element.find_all("div", {"role": "row"})
# cumulative_dict = {}
# # looping through each row in order to extract data and append it to the dictionary
# for row in div_row:
#     cumulative_dict[row.div.div.span.text] = row.find(
#         "div", {"class": "sc-fzqzEs hULauc"}).text
# # sorting the dictionary in descendind order and slicing only 10 items from the dict
# sorted_d = dict(sorted(cumulative_dict.items(),
#                        key=operator.itemgetter(1), reverse=True))
# print(dict(itertools.islice(sorted_d.items(), 10)))
# driver.close()  # closing the webdriver
