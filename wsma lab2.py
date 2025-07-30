import nltk
import spacy
import re
import emoji
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nlp = spacy.load("en_core_web_sm")


sentance = "Just spotted a 🦄 dancing under a rainbow 🌈—proof right here: https://example.com/unicorn-magic! Isn't life wonderfully absurd?"
print("Original Sentance - ",sentance)

def nltk_token(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)

    text = emoji.replace_emoji(text, replace='')  

    text = text.translate(str.maketrans('', '', string.punctuation))

    text = ' '.join(text.split())

    text = text.lower()

    tokens = word_tokenize(text)

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    


    return(filtered_tokens)


def spacy_token(text):
    doc = nlp(text)
    filtered_lemmas = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and not token.is_space]

    return( filtered_lemmas)


print("NLTK tokenization - ", nltk_token(sentance))
print("Spacy tokenization - ", spacy_token(sentance))





