from pymongo import MongoClient
from os import getenv
import pandas as pd


__all__ = ('DataBase',)


class DataBase:

    def connect_db(self):
        """ MongoDB Table Connection """
        return MongoClient(
            f"mongodb+srv://{getenv('MONGO_USER')}:{getenv('MONGO_PW')}"
            f"@{getenv('MONGO_URI')}/test?retryWrites=true&w=majority"
        ).strains_data.strains_table


if __name__ == '__main__':
    data_model = DataBase()
 