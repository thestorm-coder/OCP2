import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/the-book-of-basketball-the-nba-according-to-the-sports-guy_232/index.html"


def relative_url_to_absolute_url(url):
    url_relative = "../../media/cache/73/bb/73bbe0a70806f8a732b9a7a7a343c5ec.jpg"
    reponse = url_relative.replace("../..", "http://books.toscrape.com")
    return reponse


def str_to_int(number_str):
    if number_str == 'Five':
        return 5
    elif number_str == "Four":
        return 4
    elif number_str == "Three":
        return 3
    elif number_str == "Two":
        return 2
    elif number_str == "One":
        return 1
    elif number_str == "Zero":
        return 0


def scrap_book(url):
    response = requests.get(url)

    response.raise_for_status()
    if response.ok:

        soup = BeautifulSoup(response.content, "html.parser")

        upc = soup.select_one("table tr:nth-child(1) > td").text
        title = soup.select_one('h1').text
        prince_including_tax = soup.select_one("table > tr:nth-child(4) > td").text
        price_exluding_tax = soup.select_one("table > tr:nth-child(3) > td").text
        number_available = int(
            soup.select_one("table > tr:nth-child(6) > td").text.removeprefix("In stock (").removesuffix(" available)"))
        product_description = soup.select_one("meta:nth-child(4)")["content"]
        category = soup.select_one('div > ul > li:nth-child(3) > a').text
        review_rating = soup.select_one(".star-rating")["class"][1]
        image_url = soup.select_one("#product_gallery img")["src"]

        return {
            "upc": upc,
            "title": title,
            "price_including_tax": prince_including_tax,
            "price_excluding_tax": price_exluding_tax,
            "number_available": number_available,
            "product_description": product_description,
            "category": category,
            "review_rating": str_to_int(review_rating),
            "image_url": relative_url_to_absolute_url(image_url),
        }


if __name__ == "__main__":
    print(scrap_book(URL))
