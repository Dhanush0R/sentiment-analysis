import string
from collections import Counter
import nltk
# nltk.download()
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
class Sentiment:
    def __init__(self):
        self.cleaned_text = self.cleaning()
        self.tokenized_words = self.tokenization()
        self.final_words = self.final_word()
        self.lemma_words = self.lemmation()
        self.emotion_list = []
    def cleaning(self):
        with open('read.txt', encoding='utf-8') as text:
            text = text.read()
            lower_case = text.lower()
            cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
        return cleaned_text
# Using word_tokenize because it's faster than split()
    def tokenization(self):
        return word_tokenize(self.cleaned_text, "english")

# Removing Stop Words
    def final_word(self):
        return [word for word in self.tokenized_words if word not in stopwords.words('english')]



# Lemmatization - From plural to single + Base form of a word (example better-> good)
    def lemmation(self):
        return [WordNetLemmatizer().lemmatize(word) for word in self.final_words]

    def graph_rep(self):
        with open('emotions.txt', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
                word, emotion = clear_line.split(':')

                if word in self.lemma_words:
                    self.emotion_list.append(emotion)
        w = Counter(self.emotion_list)
        print(w)
        fig, ax1 = plt.subplots()
        ax1.bar(w.keys(), w.values())
        fig.autofmt_xdate()
        plt.savefig('graph.png')
        plt.show()

    def sentiment_analyse(self, sentiment_text):
        score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
        # print(score)
        if score['neg'] > score['pos']:
            if score['neg'] > score['neu']:
                sentiment = -1
            else:
                sentiment = 0
        else:
            if score['neu'] < score['pos']:
                sentiment = 1
            else:
                sentiment = 0

        # if score['neg'] > score['pos']:
        #     sentiment = -1
        #
        # elif score['neu'] < score['pos']:
        #     sentiment = 1
        # else:
        #     sentiment = 0

        return sentiment

#
# sent = Sentiment()
# sent.sentiment_analyse(sent.cleaned_text)
# print(sent.emotion_list)
# sent.graph_rep()


