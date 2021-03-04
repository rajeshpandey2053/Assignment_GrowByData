# Assignment_GrowByData

## Section 1: Short Questions

1. Tools used for
   Web development : Django, DjangoRestFramework, ReactJS, ReactRouter, React-Redux, HTML, Javascript, CSS
   Coding : python, C, C++, java
   Database : MYSQL, SQLite, postgreSQL, MongoDB
   Data Analysis : matplotlib, numpy , Keras, Tensorflow, scikit-learn, pandas
   Data processing : numpy, scikit-learn, pandas
   Web scraping: BeautifulSoup(worked on a project where each recipe link and direction were scraped from AllRecipes.com)
   Others : Google Dialogflow( used this to build and train chatbots),
   Nginx (used as a webserver while deploying django application in DigitalOcean)

2. The roles that i am involved in an engineering project are:
   a) Talk to the sponsors and supporters of the project
   b) Managing the project
   c) Working on the mathematics behind the project
   d) Getting your hands dirty by building the product

3. The project that i am most proud of is khushishoes.com. During the pandemic perid, my mama faced financial crisis because his shoes showroom wasnot open for months. I took the responsibility of developing an online ecommerce platform for him so that he could sustain and even thrive in those uncertain times. First time in my life, I had sleepless nights maybe i was soo much submissive in helping my family in need and also i was fully resposible for building the app from scratch,listing requirements, design, architecture, database, deploying the app.

4. The solution is in Q4section1.py

5. The following creates both the database project and the collection requests during the insertOne() operation <br />
   use project <br />
   db.requests.insertOne(
   { name: "Rajesh", Rollno: 100, hobby: ["coding","critical_thinking"] }
   );

## Section2 : Long Questions

1. a.
   use sample <br />
   db.person.count()

   b. db.person.find({(name :‘Kate Monster’, "address.city": "Chicago"})

   c. db.person.find({(name :‘Kate Monster’, "address.city": "New York"})

2. The solution is in Q2section2.py<br />
   Here," .+\/\/|www.|\..+ " , First .+\/\/ is used to match character like http:// or https://, "|" is used as a OR operator, "www." is used to match www. , finally \..+ is used to match any character preceeding by "." after the domain name.
   The answer is as follows : <br />
   http://www.stackoverflow.com stackoverflow <br />
   https://www.github.com github <br />
   www.example.net example <br />
   nepal.gov.np nepal <br />
3. The solution is in Q3section2.py

## Section3 : Project

2. a.
   The solution is in Q2a.py <br />The ans is as follows: <br />
   In Nepal, from Jan 3 to 3:35pm CET, 3 March 2021, there have been 274,294 confirmed cases of COVID-19 with 2,777 deaths.

   b. The solution is in file Q2b.py <br />
   The ans is as follows: <br />
   {'Russian Federation': '4,278,750', 'The United Kingdom': '4,188,404', 'France': '3,717,272', 'Spain': '3,130,184', 'United States of America': '28,345,585', 'Italy': '2,955,434', 'Turkey': '2,723,316', 'Germany': '2,460,030', 'Colombia': '2,255,260', 'Argentina': '2,118,676'}

   c. This question is really interesting as mousehoover needs to be automatically performed by system like human could do and data needs to be scraped. However, due to limted time, I was not able to fully accomplish this task. Also,I am still understanding the concepts inorder to scrap data from graphs using selenium library. I am sure that i am going to understand and solve this in no time.

3. The solution is in Q3section3.py . However the solution contains dummy data as graph data was not scraped tillnow.
