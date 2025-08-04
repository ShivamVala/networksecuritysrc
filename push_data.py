import os
import sys
import json 
import pandas as pd
import pymongo
import numpy as np

from dotenv import load_dotenv 
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

from networksecuritysrc.logging.logger import logging
from networksecuritysrc.exception.exception import NetworkSecurityException

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    def csv_to_json_convertor(self, file_path):
        try:
            pass
            data = pd.read_csv(file_path) 
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self,records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]    
            # self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "SHIVAM_NETWORK_SECURITY"
    Collection = "Network_Security_Data"
    networkobj = NetworkDataExtract()
    records = networkobj.csv_to_json_convertor(FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(f"Number of records inserted: {no_of_records}")