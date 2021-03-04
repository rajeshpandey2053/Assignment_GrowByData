# Assignment_GrowByData

## Section 1: Short Questions

1. Tools used for
   Web development : Django, DjangoRestFramework, ReactJS, ReactRouter, React-Redux, HTML, Javascript, CSS
   Coding : Keras, numpy, scikit-learn, matplotlib,
   Database : SQL, SQLite, postgreSQL
   Data Analysis : matplotlib, numpy , keras, Tensorflow
   Data processing : numpy, scikit-learn
   Web scraping: BeautifulSoup

2. The roles that i am involved in an engineering project are:
   a) Talk to the sponsors and supporters of the project
   b) Managing the project
   c) Working on the mathematics behind the project
   d) Getting your hands dirty by building the product

3. The project that i am most proud of is khushishoes.com. During the pandemic perid, my mama faced finanial crisis because his shoes showroom wasnot open for months. I took the responsibility of developing an online ecommerce platform for him so that he could sustain and even thrive in those uncertain times. First time in my life, I had sleepless nights maybe i was soo much submissive in helping my family in need and also i was fully resposible for building the app from scratch,listing requirements, design, architecture, database, deploying the app.

4. sum the integer elements an array using the map() function
   elements = [[1, 2, 3], [4, 5, 6], [2, 3, 4]] # Delcare and defining an array
   total_sum = list(map(sum, elements)) # Using map() and sum() inbuilt function to find sum of each integer array and store in a list.
   print(total_sum) # print the sum of list

5. The following creates both the database myNewDatabase and the collection myCollection during the insertOne() operation
   use project
   db.requests.insertOne(
   { name: "Rajesh", Rollno: 100, hobby: ["dancing","singing"] }
   );

## Section2 : Long Questions

1. a.
   use sample
   db.person.count()

   b. db.person.find({(name :‘Kate Monster’, "address.city": "Chicago"})

   c. db.person.find({(name :‘Kate Monster’, "address.city": "Chicago"})

2.
3. import requests
   #first try to find if html file can be scraped within 0.075
   try:
   scrapedhtml = requests.get(
   "https://www.google.com/search?q=nike+shoes.", timeout=0.075).text
   #if exception occurs then write timeout error into a file
   except requests.Timeout as e:
   print("OOPS!! Timeout Error")
   scrapedhtml = "Oops Timeout Error"
   #in both the cases write html file if exception is not raised else if raised then write timeout error into a htmlfile
   finally:
   record_file = open('htmlfile.html', 'w')
   record_file.write(scrapedhtml)
   record_file.close()

## Section3 : Project

2. a. The solution is in Q2a.py
   The ans is as follows:
   In Nepal, from Jan 3 to 3:35pm CET, 3 March 2021, there have been 274,294 confirmed cases of COVID-19 with 2,777 deaths.

b. The solution is in file Q2b.py
The ans is as follows:
{'Russian Federation': '4,278,750', 'The United Kingdom': '4,188,404', 'France': '3,717,272', 'Spain': '3,130,184', 'United States of America': '28,345,585', 'Italy': '2,955,434', 'Turkey': '2,723,316', 'Germany': '2,460,030', 'Colombia': '2,255,260', 'Argentina': '2,118,676'}
