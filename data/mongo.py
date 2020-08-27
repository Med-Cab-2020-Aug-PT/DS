from os import getenv
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# DB_USER = getenv("MONGO_USER")
# DB_PW = getenv("MONGO_PW")
# DB_URI = getenv("MONGO_URI")

# client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PW}@{DB_URI}/strains?retryWrites=true&w=majority")
# DB = client.strain_table
# table = DB.strain_table
# print(table)

def create_db(file_name: str):
    """ Creates and populates MongoDB """
    load_dotenv()

    DB_USER = getenv("MONGO_USER")
    DB_PW = getenv("MONGO_PW")
    DB_URI = getenv("MONGO_URI")

    client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PW}@{DB_URI}/strains?retryWrites=true&w=majority")
    DB = client.strains_data
    table = DB.strains_table
    print(table)

    df = pd.read_csv(file_name)
    data = df.to_dict(orient='records')
    for item in data:
        item['Effects'] = item['Effects'].split(',')
        item['Flavors'] = item["Flavors"].split(',')
        item['Nearest'] = [
            data[int(idx)]['Name'] for idx in item['Nearest'].split(',')
        ]
    table.insert_many(data)

if __name__ == "__main__":
    create_db('cannabis.csv')
