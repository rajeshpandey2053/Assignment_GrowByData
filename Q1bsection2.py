from pymongo import MongoClient

data =


def main():
    print('Connecting to mongodb')
    client = MongoClient('localhost', 27017)

    db = client['Covid']

    collection = db['Nepal']

    res = collection.insert_many(data)

    print('Inserted ids')
    print(res.inserted_ids)


if __name__ == "__main__":
    main()
