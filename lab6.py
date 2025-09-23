import nltk
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
reviews = [
    "I absolutely love this phone, the camera is amazing!",
    "The battery life is terrible and it keeps overheating.",
    "It's okay, does the job but nothing special.",
    "Excellent build quality and very fast performance.",
    "Worst purchase ever! Completely useless after a week.",
    "Pretty decent for the price, but could be better."
 ]
# print("Vader Sentiment Analysis")
# vader = SentimentIntensityAnalyzer()
# for review in reviews:
#     scores = vader.polarity_scores(review)
#     print(f"Review : {review}")
#     print(f"Scores: {scores}")
#     if scores['compound']>=0.05:
#         print("Positive Sentiment")
#     elif scores['compound']<=-0.05:
#         print("Negative Sentiment")
#     else:
#         print("Neutral Sentimnet")
#     print("-" * 50)

# from textblob import TextBlob

# print("Textblob sentiment Analysis")

# for review in reviews:
#     blob = TextBlob(review)
#     polarity = blob.sentiment.polarity
#     subjectivity = blob.sentiment.subjectivity
#     print(f"Review: {review}")
#     print(f"Subjectivity : {subjectivity}, Polarity : {polarity}")
#     if polarity>0:
#         print("Positive Sentiment")
#     elif polarity<0:
#         print("Negative Sentiment")
#     else :
#         print("Neutral Sentiment")
#     print("-" * 50)




import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob",last=True)

print(nlp.pipe_names)

print("Spacy Sentiment Analysis")

for review in reviews:
    doc = nlp(review)
    print(f"Review: {review}")
    print(f"Polarity: {doc._.polarity}, Subjectivity: {doc._.subjectivity}")
    if doc._.polarity>0:
        print("Positive Sentiment")
    elif doc._.polarity<0:
        print("Negative Sentiment")
    else :
        print("Neutral Sentiment")
    print("-"*50)

