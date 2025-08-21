import os
import logging
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.cursor import Cursor


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
        self.client_con = self.client()
            
        logger.debug(f"Database connection parameters set: DB_HOST:{self.HOST}, MONGO_DATABASE:{self.DATABASE}")

    def client(self) -> MongoClient:
        """
        Create a MongoDB client.
        """
        self.connection_string = f"mongodb+srv://{self.USER}:{self.PASS}@{self.HOST}/"
        client:MongoClient = MongoClient(self.connection_string)
        return client
    
    def get_database(self) -> Database:
        """Create a database connection.""" 
        db: Database = self.client_con[self.DATABASE]
        logger.debug("Database connection successful.")
        return db

    def get_collection(self) -> Collection:
        """
        Fetch all records from the specified table.
        """
        logger.debug(f"Fetching all records from collection: {self.COLLECTION}")

        db: Database = self.get_database()
        collection: Collection = db[self.COLLECTION]
        return collection
    
    def get(self ) -> Cursor:
        """Fetch  from the database."""
        collection:Collection = self.get_collection()
        return collection.find({},{'_id':0})
    
    

if __name__ == "__main__":
    dataLoader = DataLoader()
    all = dataLoader.get()
    print(all)
