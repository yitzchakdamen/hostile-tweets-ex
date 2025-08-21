import pandas as pd
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from json import loads, dumps
from analysis import Analysis

class Processing:
    
    def __init__(self, retrieval_df: pd.DataFrame) -> None:
        self.df:pd.DataFrame = retrieval_df
        
    def the_rarest_word(self, col_name:str="Text") -> None:
        """Find the rarest word in a given text column."""
        self.df["rarest_word"] = self.df[col_name].apply(Analysis.rarest_word)
        
    def the_emotion_text(self) -> None:
        """Analyze the sentiment of the text."""
        self.df["sentiment"] = self.df["Text"].apply(Analysis.analyze_sentiment)
        self.df["sentiment"] = self.df["sentiment"].apply(Analysis.sentiment_category)

    def weapons_detected(self, file_url:str= "data/weapons.txt") -> None:
        """Detect weapons mentioned in the text."""
        self.df["weapons_detected"] = self.df["Text"].apply(Analysis.weapons_detected)

    def saving_as_json_format(self) -> dict:
        """Save the DataFrame as a JSON format."""
        self.df.rename(columns={ "TweetID": "id", "Text": "original_text"}, inplace=True)
        return loads(self.df.to_json(orient="records"))


