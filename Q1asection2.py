from pymongo import MongoClient

# data = [{
#     "name": 'Kate Monster',
#     "ssn": '123-456-7890',
#     "addresses": [
#         {"street": '123 Sesame St', "city": 'Anytown', "cc": 'USA'},
#         {"street": '123 Avenue Q', "city": 'New York', "cc": 'USA'}
#     ]
# }, {
#     "name": 'Hari',
#     "ssn": '122-452-7390',
#     "addresses": [
#         {"street": '123 hari St', "city": 'Chicago', "cc": 'USA'},
#         {"street": '123 Avenue Q', "city": 'New York', "cc": 'USA'}
#     ]
# }
# ]


# def main():
#     print('Connecting to mongodb')
#     client = MongoClient('localhost', 27017)
#     # Getting database instance
#     db = client['sample']
#     print("Database created........")
#     # Verification
#     print("List of databases after creating new one")
#     print(client.list_database_names())
#     # collection = db['person']

#     # res = collection.insert_many(data)


# if __name__ == "__main__":
#     main()


from pymongo import MongoClient

# Creating a pymongo client
client = MongoClient('localhost', 27017)

# Getting the database instance
db = client['mydb']

# Creating a collection
coll = db['example']

# Inserting document into a collection
data = [
    {
        "_id": "101",
        "name": "Ram",
        "age": "26",
        "city": "Hyderabad"
    },
    {
        "_id": "102",
        "name": "Rahim",
        "age": "27",
        "city": "Bangalore"
    },
    {
        "_id": "103",
        "name": "Robert",
        "age": "28",
        "city": "Mumbai"
    }
]
res = coll.insert_many(data)
print("Data inserted ......")
print(res.inserted_ids)
