from bs4 import BeautifulSoup


# with open(r"web scrapping\bs4-start\website.html","r") as file:
#     content= file.read()
# soup= BeautifulSoup(content, "html.parser") 


# # print(soup.a)
# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.get("href") )

import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []

for article in articles:
    a_tag = article.find("a")

    title = a_tag.getText()
    article_texts.append(title)

    
    link = a_tag.get("href")
    article_links.append(link)

upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", class_="score")]
print(upvote)

largest_number = max(upvote)
print(largest_number)
largest_index = upvote.index(largest_number)
print(article_texts[largest_index])
# print(upvote)
# print(article_texts)

# print(article_links)


