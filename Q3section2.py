import requests
# first try to find if html file can be scraped within 0.075
try:
    scrapedhtml = requests.get(
        "https://www.google.com/search?q=nike+shoes.", timeout=0.075).text
    # if exception occurs then write timeout error into a file
except requests.Timeout as e:
    print("OOPS!! Timeout Error")
    scrapedhtml = "Oops Timeout Error"
    # in both the cases write html file, if exception is not raised, then write the scraped contents to the htmlfile else write timeout error into a htmlfile
finally:
    record_file = open('htmlfile.html', 'w')
    record_file.write(scrapedhtml)
    record_file.close()
