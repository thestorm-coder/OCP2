import requests
from bs4 import BeautifulSoup


def scrap_main_category():
    """ permet d'obtenir tous les liens des différents catégories du site wwww.booktoscrape.com """

    for link in generate_cat_links():
        print(link)
        reponse = requests.get(link)

        if reponse.ok:
            soup = BeautifulSoup(reponse.content, "html.parser")

            for h3 in soup.findAll("h3"):
                link = h3.find("a")["href"]
                yield f"http://books.toscrape.com/catalogue/{link}"
        else:
            break


def generate_cat_links():
    """une fonction génératrice qui renvoie l'ensemble des urls du site et leurs composants"""
    nb = 0
    while True:
        nb += 1
        yield f"http://books.toscrape.com/catalogue/page-{nb}.html"
