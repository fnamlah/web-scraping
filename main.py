from bs4 import BeautifulSoup
# import lxml
with open("website.html") as file:
    contents = file.read()

# How to parse: BeautifulSoup(website url, "html.parser") or (website url, "lmxl")
soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# getting the first anchor tag:
# print(soup.a)
# How to get ALL tags or images or paragraphs:
all_anchor_tag = soup.find_all(name="a")
# print(all_anchor_tag)

for tag in all_anchor_tag:
    pass
    # print(tag.getText())
    # print(tag.get("href"))

# finding an element by its ID
heading = soup.find(name="h1", id="name")
print(heading)

# finding an element by its CLASS using class_ instead of class because class is reserved in Python:
section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))

# narrowing down an element:
company_url = soup.select_one(selector="p a")
# print(company_url)

# using CSS Selectors:
name = soup.select_one(selector="#name")
# print(name)

headings = soup.select(selector=".heading")
# print(headings)
