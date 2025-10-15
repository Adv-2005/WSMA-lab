from bs4 import BeautifulSoup
from collections import Counter
import re

spammy_html = """
 <html>
 <head><title>Cheap Shoes Online</title></head>
 <body style="background-color:white">
 <h1>Buy Cheap Shoes Online</h1>
 <p>Cheap shoes cheap shoes cheap shoes cheap shoes cheap shoes!
 Best cheap shoes for sale. Cheap shoes now!</p>
 <p style="color:white">Hidden text that search engines might index but 
users can't see</p>
 <!-- Simulated cloaking: content for bots -->
 <div id="bot-content">
 <p>Exclusive shoes for search engines with many keyword repeats.</p>
 </div>
 </body>
 </html>
 """

soup = BeautifulSoup(spammy_html, "html.parser")
text = soup.get_text(separator=" ").lower()
words = re.findall(r"\w+", text)

def detect_keyword_stuffing(words, threshold=0.05):
    total_words = len(words)
    word_counts = Counter(words)
    stuffed_keywords = {word: count for word, count in 
word_counts.items()
                        if (count / total_words) > threshold and 
len(word) > 3}
    return stuffed_keywords
stuffed = detect_keyword_stuffing(words, threshold=0.15)  
print("Keyword stuffing detected:", stuffed)

hidden_texts = []
for tag in soup.find_all(style=True):
    style = tag['style'].lower()
    if "display:none" in style or "color:white" in style or "font-size:0" in style:
        hidden_texts.append(tag.get_text(strip=True))
print("Hidden text detected:", hidden_texts)


bot_view = soup.find("div", {"id": "bot-content"}).get_text(strip=True)
user_view = soup.get_text(strip=True).replace(bot_view,"")
if bot_view not in user_view:
    print("Possible cloaking detected! Bot content differs from user content.")