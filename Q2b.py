import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import operator
import itertools
# url of the page we want to scrape
url = "https://covid19.who.int/table"

# initiating the webdriver. Parameter includes the path of the webdriver.
driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get(url)

# this is just to ensure that the page is loaded
time.sleep(5)

html = driver.page_source

# this renders the JS code and stores all
# of the information in static HTML code.

# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
# finding the container element which has all the rows of cumulative data
rowgroup_element = soup.find('div', {"role": "rowgroup"})
# listing all the rows which contains individual cumulative values of each country
div_row = rowgroup_element.find_all("div", {"role": "row"})
cumulative_dict = {}
# looping through each row in order to extract data and append it to the dictionary
for row in div_row:
    cumulative_dict[row.div.div.span.text] = row.find(
        "div", {"class": "sc-fzqzEs hULauc"}).text
# sorting the dictionary in descendind order and slicing only 10 items from the dict
sorted_d = dict(sorted(cumulative_dict.items(),
                       key=operator.itemgetter(1), reverse=True))
print(dict(itertools.islice(sorted_d.items(), 10)))
driver.close()  # closing the webdriver
