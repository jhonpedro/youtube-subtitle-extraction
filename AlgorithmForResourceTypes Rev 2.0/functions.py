from nltk.stem import RSLPStemmer
from nltk.corpus import stopwords

def Format(subtitle):
    subtitle = subtitle.lower()

    subtitle = subtitle.replace(" i ", " ")
    subtitle = subtitle.replace(".", " ")
    subtitle = subtitle.replace(",", " ")
    subtitle = subtitle.replace("?", " ")
    subtitle = subtitle.replace("!", " ")
    subtitle = subtitle.replace(":", " ")

    subtitle = subtitle.split()

    return subtitle

def Stemming(subtitle):
    stemmer = RSLPStemmer()
    toReturn = []
    for word in subtitle:
        toReturn.append(stemmer.stem(word.lower()))
    return toReturn

def RemoveStopWords(subtitle):
    ListStopwords = stopwords.words('portuguese')
    toReturn = []
    for word in subtitle:
        if word not in ListStopwords:
            toReturn.append(word)
    return toReturn