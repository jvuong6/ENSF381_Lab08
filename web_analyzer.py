import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

headings = len(soup.find_all(re.compile("^h")))
print(f"Headings: {headings}")

links = len(soup.find_all("a"))
print(f"Links: {links}")

paragraphs = len(soup.find_all("p"))
print(f"Paragraphs: {paragraphs}")

keyword = str(input("Input Keyword to Search For: "))
soup_str = soup.get_text()

words = re.findall(r'\b\w+\b', soup_str.lower())
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

keyword_count = word_counts.get(keyword)
print(f"Keyword Count: {keyword_count}")

sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
print("Top 5 Words")
print(sorted_words[:5])


para = soup_str.split("\n")
p_lengths = {}
for paragraph in para:
    if len(paragraph) >= 5:
        p_lengths[paragraph] = p_lengths.get(paragraph, 0) + len(paragraph)
sorted_paragraphs = sorted(p_lengths.items(), key=lambda item: item[1], reverse=True)
print(sorted_paragraphs[:1])
    
labels = ['Headings', 'Links', 'Paragraphs']
values = [headings, links, paragraphs]
plt.bar(labels, values)
plt.title('Group 47')
plt.ylabel('Count')
plt.show()

