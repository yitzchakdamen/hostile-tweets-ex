from processor import Processing
from fetcher import DataLoader
from pymongo.cursor import Cursor
import pandas as pd


class Management:
    
    def __init__(self) -> None:
        self.dataLoader:DataLoader = DataLoader()

    def start(self):
        retrieval:Cursor = self.retrieval_management()
        df:pd.DataFrame = self.conversion_to_dataframe(retrieval)
        processing: dict = self.processing_management(df)
    
    def retrieval_management(self) -> Cursor:
        return self.dataLoader.get()
    
    def processing_management(self, df:pd.DataFrame) -> dict:
        processing:Processing = Processing(df)
        return processing.saving_dict_format()
        
    
    def conversion_to_dataframe(self, object_cursor: Cursor) -> pd.DataFrame:
        return pd.DataFrame(object_cursor)