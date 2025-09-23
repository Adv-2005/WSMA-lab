from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.util import ngrams
import nltk
import pandas as pd

nltk.download('punkt')

docs = [
    "Web analytics is essential for understanding traffic.",
    "TF-IDF highlights important terms across documents.",
    "Natural language processing helps extract insights from text."
 ]

def lexical_diversity(text):
    tokens = nltk.word_tokenize(text.lower())
    return len(set(tokens)) / len(tokens)

print("=== Lexical Diversity ===")
for i, doc in enumerate(docs):
    print(f"Doc {i+1}: {lexical_diversity(doc):.2f}")

for i, doc in enumerate(docs):
    tokens = nltk.word_tokenize(doc.lower())
    print(f"\n=== N-grams for Doc {i+1} ===")
    for n in [1,2,3] :
        ng_list = list(ngrams(tokens,n))
        print(f"{n}-grams: {ng_list}")

vectorizer =TfidfVectorizer()
X = vectorizer.fit_transform(docs)
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print("\n=== TF-IDF Matrix ===")
print(df)

print("idx, row \n=== Top TF-IDF Terms per Document ===")
for idx, row in df.iterrows():
    top_terms =row.sort_values(ascending=False).head(3)
    print(f"Doc {idx+1} for term, score :") 
    for term, score in top_terms.items():
        print(f"  {term}: {score:.3f}")