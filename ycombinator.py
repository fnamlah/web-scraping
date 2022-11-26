from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text
# print(yc_webpage)
soup = BeautifulSoup(yc_webpage, "html.parser")
# print(soup.title)

articles = soup.find_all(name="span", class_="titleline")
# print(articles)
article_text = [article.find(name="a").get_text() for article in articles]
article_link = [article.find(name="a").get("href") for article in articles]
article_score = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


print(article_text)
print(article_link)
print(article_score)

index_of_max_score = article_score.index(max(article_score))
print(index_of_max_score)
print(article_text[index_of_max_score])
print(article_link[index_of_max_score])
