import requests
from bs4 import BeautifulSoup
import json

# Fetch and parse the webpage
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract h1, h2, h3 headlines
headlines = soup.find_all(['h3', 'h4', 'h5', 'h6'])

# Get text content
headline_texts = [headline.get_text() for headline in headlines]

# Slice to top 10
top_10_headlines = headline_texts[:10]

# Store in JSON
data = {"headlines": top_10_headlines}
with open("headlines1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"{len(top_10_headlines)} top headlines saved to headlines.json")