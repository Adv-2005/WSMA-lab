import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt
from urllib.parse import urlparse, urljoin
import pandas as pd

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

links_data = []
parsed_base = urlparse(url)

for a_tag in soup.find_all("a", href=True):
    href = a_tag["href"]
    full_url = urljoin(url,href)
    parsed_href = urlparse(full_url)
    
    if parsed_href.netloc == parsed_base.netloc:
        link_type = "internal"
    else:
        link_type = "external"
        
    links_data.append({
        "anchor_text": a_tag.get_text(strip=True),
        "url": full_url,
        "link_type": link_type
    })
    
links_df = pd.DataFrame(links_data)
print("Sample links extracted:")
print(links_df.head())

internal_count = (links_df["link_type"] == "internal").sum()
external_count = (links_df["link_type"] == "external").sum()
links_df["anchor_length"] = links_df["anchor_text"].apply(len)
print(f"Internal Links: {internal_count}")
print(f"External Links: {external_count}")
print("Average Anchor Text Length:", links_df["anchor_length"].mean())

pages = {
    "Home": ["About", "Products", "Contact"],
    "About": ["Home", "Products"],
    "Products": ["Home", "Contact"],
    "Contact": ["Home"]
 }
G = nx.DiGraph()
for page, out_links in pages.items():
    for dest in out_links:
        G.add_edge(page, dest)

pagerank_scores = nx.pagerank(G, alpha=0.85)
print("PageRank Scores:")
for page, score in pagerank_scores.items():
    print(f"{page}: {score:.4f}")

plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue",node_size=2000, arrowsize=20)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): '' for u, v  in G.edges()})
plt.title("Website Link Graph")
plt.show()