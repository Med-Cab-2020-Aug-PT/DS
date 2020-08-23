import os
from pymongo import MongoClient
import pandas as pd

DB_USER = os.getenv("MONGO_USER", default="Check settings")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="Check settings")
CLUSTER = os.getenv("MONGO_CLUSTER", default="Check settings")

client = MongoClient("mongodb+srv://{MONGO_USER}:{MONGO_PW}@strains.aofhk.mongodb.net/{MONGO_CLUSTER}?retryWrites=true&w=majority")
DB = client.test
