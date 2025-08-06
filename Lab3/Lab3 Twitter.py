import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer
from collections import Counter
import string
import spacy

nlp = spacy.load("en_core_web_sm")


with open(r"C:\Users\maheit\Desktop\Aditya Varshney\sample_tweets.txt", "r", encoding="utf-8") as file:
    text = file.read()

clean_text = text.lower().translate(str.maketrans('', '', string.punctuation))


tokens = word_tokenize(clean_text)
tokens = [word for word in tokens if word.isalpha()]


porter = PorterStemmer()
snowball = SnowballStemmer("english")

porter_stems = [porter.stem(word) for word in tokens]
snowball_stems = [snowball.stem(word) for word in tokens]


porter_freq = Counter(porter_stems)
snowball_freq = Counter(snowball_stems)


doc = nlp(clean_text)
lemmas = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
lemma_freq = Counter(lemmas)

top_porter = porter_freq.most_common(10)
top_snowball = snowball_freq.most_common(10)
top_lemmas = lemma_freq.most_common(10)


print("Top 10 Porter Stemmer Words:")
for word, freq in top_porter:
    print(f"{word}: {freq}")

print("\nTop 10 Snowball Stemmer Words:")
for word, freq in top_snowball:
    print(f"{word}: {freq}")

print("\nTop 10 Lemmatized Words:")
for word, freq in top_lemmas:
    print(f"{word}: {freq}")