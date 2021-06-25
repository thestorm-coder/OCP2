from scrap_category import scrap_main_category
from scrap_book import scrap_book
import requests


def scrap_website():
    books = {}
    for book_url in scrap_main_category():
        print(book_url)
        book = scrap_book(book_url)
        response = requests.get(book["image_url"])
        upc = book['upc']
        with open(f"img/{upc}.jpg", "wb") as file:
            file.write(response.content)
        print(book["image_url"])
        category = book["category"]
        if category not in books:
            books[category] = []
        books[category].append(book)
    print(len(books))


if __name__ == "__main__":
    scrap_website()
