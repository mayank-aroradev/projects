from bs4 import BeautifulSoup


with open(r"web scrapping\bs4-start\website.html","r") as file:
    content= file.read()
soup= BeautifulSoup(content, "html.parser") 


# print(soup.a)
all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.get("href") )