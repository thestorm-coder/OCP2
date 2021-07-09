from scrap_category import scrap_main_category
from scrap_book import scrap_book
import requests
import csv
import time


def scrap_website():
    start_time = time.time()
    categories = {}
    for book_url in scrap_main_category():
        print(book_url)
        book = scrap_book(book_url)
        response = requests.get(book["image_url"])
        upc = book['upc']
        with open(f"img/{upc}.jpg", "wb") as file:
            file.write(response.content)

        category = book["category"]
        if category not in categories:
            categories[category] = []
        categories[category].append(book)

    for category, books in categories.items():
        with open(f"CSV/{category}.csv", 'w', encoding="utf-8-sig") as csvfile:
            fieldnames = [
                "upc", "title", "price_including_tax",
                "price_excluding_tax", "number_available",
                "product_description", "category", "review_rating",
                "image_url"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for book in books:
                writer.writerow(book)

    end_time = time.time()
    print(f"Elapsed time: {end_time - start_time} s")


if __name__ == "__main__":
    scrap_website()
