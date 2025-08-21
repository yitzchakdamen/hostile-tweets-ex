from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer


class Analysis:
        
    @staticmethod
    def rarest_word(word:str) -> str:
        """Find the rarest word in a given text."""
        return Counter(word.split(" ")).most_common(1)[0][0]

    @staticmethod
    def analyze_sentiment(tweet: str) -> float:
        """Analyze the sentiment of a tweet."""
        return SentimentIntensityAnalyzer().polarity_scores(tweet)["compound"]
    
    @staticmethod
    def sentiment_category(num:float) -> str:
        """Categorize the sentiment score."""
        if num <= 0.5: return "Positive"
        elif num < 0.5 and num > -0.5: return "Neutral"
        else: return "Negative"

    @staticmethod
    def get_list_of_weapons(file_url: str) -> list[str]:
        """Get a list of weapons from a file."""
        with open(file_url, "r", encoding="utf-8") as f:
            file_content = f.read()
        return file_content.split("\n")

    @staticmethod
    def weapons_detected(text: str, file_url: str) -> str:
        """Detect weapons mentioned in the text."""
        return " ".join([weapon for weapon in Analysis.get_list_of_weapons(file_url) if weapon in text.split(" ")])