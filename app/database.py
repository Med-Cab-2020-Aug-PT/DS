from pymongo import MongoClient
from os import getenv
import pandas as pd


__all__ = ('DataBase',)


class DataBase:

    def connect_db(self):
        """ MongoDB Table Connection """
        return MongoClient(
            f"mongodb+srv://{getenv('MONGODB_USER')}:{getenv('MONGODB_PASS')}"
            f"@{getenv('MONGODB_URI')}/test?retryWrites=true&w=majority"
        ).medcabin.strain_table

    def read_csv(self):
        return pd.read_csv('data/cannabis.csv')

    def find(self, query: dict) -> dict:
        return self.connect_db().find_one(query)


if __name__ == '__main__':
    data_model = DataBase()
    data_model.connect_db()
