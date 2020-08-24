from os import getenv
from pymongo import MongoClient
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

def create_db(file_name: str):
    """ Creates and populates MongoDB """

    client = MongoClient("mongodb+srv://med_cab:K6cSRmWVV3PA40xf@strains.aofhk.mongodb.net/strains?retryWrites=true&w=majority")
    DB = client.strain_table
    table = DB.strain_table

    df = pd.read_csv(file_name)
    data = df.to_dict(orient='records')
    table.insert_many(data)

if __name__ == "__main__":
    create_db('cannabis.csv')
