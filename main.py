import requests
from bs4 import BeautifulSoup

link = "http://books.toscrape.com/catalogue/category/books/travel_2/index.html"
response = requests.get(link)
website = response.text
soup = BeautifulSoup(website, "html.parser")
print(soup.prettify)

strong_tags= soup.find_all('strong')
result_counts = strong_tags[1].text
print(result_counts)

site_title = soup.find(name="title")
print(site_title)

book_price = soup.find_all(name="p", class_="price_color")

for price_element in book_price:
    price = price_element.text
    print(price)

book_link = soup.find_all(name="a")
for link in book_link:
    books = link.getText()
    print(books)

book_name=soup.find_all(name="h3")
print(book_name)

titles = [h3.a['title'] for h3 in soup.find_all(name="h3")]
for title in titles:
    print(title)
with open("books.txt", mode="w", encoding="utf-8") as file:
    for book in titles:
        file.write(f"{book}\n")
