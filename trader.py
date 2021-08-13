from bs4 import BeautifulSoup
import requests


def main():
    page = requests.get("https://backpack.tf/")
    if page.status_code != 200:
        exit()
    scraptf = BeautifulSoup(page.content, 'html.parser')
    print(scraptf.prettify())


main()
