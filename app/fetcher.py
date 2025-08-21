import os
import logging
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor
import pandas as pd


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



class DataLoader:
    
    def __init__(self) -> None:
        """Initialize database connection parameters."""
        self.HOST:str = os.getenv("HOST", "iranmaldb.gurutam.mongodb.net") 
        self.PORT:str = os.getenv("PORT", "27017")
        self.USER: str = os.getenv("USER", "IRGC")
        self.PASS:str =  os.getenv("PASS", "iraniraniran")
        self.DATABASE:str = os.getenv("DATABASE", "IranMalDB") 
        self.COLLECTION:str = os.getenv("COLLECTION", "tweets")

        logger.debug(f"Database connection parameters set: HOST:{self.HOST}, DATABASE:{self.DATABASE}, COLLECTION:{self.COLLECTION}, USER:{self.USER}, PASS:{self.PASS}")

    def client(self) -> MongoClient:
        """
        Create a MongoDB client.
        """
        self.connection_string = f"mongodb+srv://{self.USER}:{self.PASS}@{self.HOST}/"
        client:MongoClient = MongoClient(self.connection_string)
        return client

    def get_database(self, client: MongoClient) -> Database:
        """Create a database connection."""
        db: Database = client[self.DATABASE]
        logger.debug("Database connection successful.")
        return db

    def get_collection(self, db: Database) -> Collection:
        """Get the specified collection from the database."""
        logger.debug(f"Fetching all records from collection: {self.COLLECTION}")
        return db[self.COLLECTION]

    def get_data(self ) -> pd.DataFrame:
        """Fetch data from the database."""
        client: MongoClient = self.client()
        db: Database = self.get_database(client)
        collection: Collection = self.get_collection(db)
        result: Cursor = collection.find({},{'_id':0})
        df = pd.DataFrame(result)
        client.close()
        return df

