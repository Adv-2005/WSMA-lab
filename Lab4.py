#using spacy do POS and NER then using matplotlib do visualization
from collections import Counter
import spacy
import matplotlib.pyplot as plt
nlp = spacy.load("en_core_web_sm")
text = "Google was founded by Larry Page and Sergey Brin while they were Ph.D. students at Stanford University. The company is headquartered in Mountain View, California.In 2020, Google’s parent company Alphabet reported revenues of over $180 billion."

doc = nlp(text)

# print("POS tags: ")

# for token in doc:
#     print(f"{token.text}: {token.pos_}")

# print ("Entities: ")

# for ent in doc.ents:
#     print(f"{ent.text}: {ent.label_}")

pos_tags = [token.pos_ for token in doc if not token.is_space and not token.is_punct]
pos_freq = Counter(pos_tags)

# POS bar
plt.figure(figsize=(8,5))
plt.bar(pos_freq.keys(), pos_freq.values(), color='lightgreen')
plt.xlabel('POS Tag')
plt.ylabel('Frequency')
plt.title('Part-of-Speech Tag Frequency')
plt.xticks(rotation=45)
plt.show()

entity_labels = [ent.label_ for ent in doc.ents]
label_freq = Counter(entity_labels)

# NER bar
plt.figure(figsize=(8,5))
plt.bar(label_freq.keys(), label_freq.values(), color='skyblue')
plt.xlabel('Entity Type')
plt.ylabel('Frequency')
plt.title('Named Entity Frequency')

plt.show()

# POS Pie chart
plt.figure(figsize=(8,8))
plt.pie(
    pos_freq.values(), 
    labels=pos_freq.keys(), 
    autopct='%1.1f%%', 
    # startangle=140,
    colors=plt.cm.Paired.colors
)
plt.title('Part-of-Speech Tag Distribution')
plt.axis('equal')  
plt.show()

# NER pie chart
plt.figure(figsize=(8,8))
plt.pie(
    label_freq.values(),
    labels=label_freq.keys(),
    autopct='%1.1f%%',
    # startangle=140,
    colors=plt.cm.Paired.colors
)
plt.title('Named Entity Type Distribution')
plt.axis('equal')  
plt.show()