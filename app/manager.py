from processor import Processing
from fetcher import DataLoader
from pymongo.cursor import Cursor
import pandas as pd
import nltk


class Management:
    
    def __init__(self) -> None:
        self.dataLoader:DataLoader = DataLoader()
        # nltk.download('vader_lexicon')

    def start(self) -> dict:
        df:pd.DataFrame = self.retrieval_management()
        processing: dict = self.processing_management(df)
        return processing
    
    def retrieval_management(self) -> pd.DataFrame:
        return self.dataLoader.get_data()
    
    def processing_management(self, df:pd.DataFrame) -> dict:
        processing:Processing = Processing(df)
        processing.the_rarest_word()
        processing.the_emotion_text()
        processing.weapons_detected()
        return processing.saving_as_json_format()
        
    def conversion_to_dataframe(self, object_cursor: Cursor) -> pd.DataFrame:
        return pd.DataFrame(object_cursor)