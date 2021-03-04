from pymongo import MongoClient

data = [
    {
        "date": '2020-12-01',
        "change": "12",
        "percentChange": "8",
    },
    {
        "date": '2020-12-02',
        "change": "9",
        "percentChange": "5"
    }
]


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
