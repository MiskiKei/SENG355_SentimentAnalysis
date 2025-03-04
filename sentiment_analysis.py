import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.sentiment import SentimentIntensityAnalyzer


class SentimentAnalyzer:
    def __init__(self):
        self.sia = SentimentIntensityAnalyzer()
        self.stemmer = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        tokens = word_tokenize(text.lower())

        processed_tokens = []
        for word in tokens:
            if word.isalnum() and word not in stopwords.words("english"):
                stemmed_word = self.stemmer.stem(word)
                lemmatized_word = self.lemmatizer.lemmatize(stemmed_word, wordnet.VERB)
                processed_tokens.append(lemmatized_word)

        return " ".join(processed_tokens)

    def analyze_sentiment(self, text):
        processed_text = self.preprocess_text(text)

        scores = self.sia.polarity_scores(processed_text)
        sentiment = "Positive" if scores["compound"] > 0 else "Negative" if scores["compound"] < 0 else "Neutral"
        return sentiment, scores

