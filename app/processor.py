import pandas as pd
from collections import Counter
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from json import loads, dumps

class Processing:
    
    def __init__(self, retrieval_df: pd.DataFrame) -> None:
        self.df:pd.DataFrame = retrieval_df
        
    def the_rarest_word(self, col_name:str="Text") -> None:
        """Find the rarest word in a given text column."""
        
        def rarest_word(word:str) -> str:
            return Counter(word.split(" ")).most_common(1)[0][0]
        
        self.df["rarest_word"] = self.df[col_name].apply(rarest_word)
        
    def the_emotion_text(self) -> None:
        
        def rating(num:float) -> str:
            if num <= 0.5: return "Positive"
            elif num < 0.5 and num > -0.5: return "Neutral"
            else: return "Negative"

        def emotion(tweet: str) -> float:
            nltk.download('vader_lexicon')
            return SentimentIntensityAnalyzer().polarity_scores(tweet)["compound"]

        self.df["emotion"] = self.df["Text"].apply(emotion)
        self.df["sentiment"] = self.df["emotion"].apply(rating)

    def weapons_detected(self, file_url:str= "data/weapons.txt") -> None:
        
        def get_list_of_weapons(file_url: str) -> list[str]:
            with open(file_url, "r", encoding="utf-8") as f:
                file_content = f.read()
            return file_content.split("\n")

        def weapons_detected(text: str) -> str:
            return " ".join([weapon for weapon in get_list_of_weapons(file_url) if weapon in text.split(" ")])

        self.df["weapons_detected"] = self.df["Text"].apply(weapons_detected)

    def saving_as_json_format(self) -> dict:
        return loads(self.df.to_json(orient="records"))

    