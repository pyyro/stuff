'''
i dont know why the fuck this doesnt work
fuck u amazon and your retarded website
'''
import requests
from bs4 import BeautifulSoup


def listResults(keyword):
    url = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + keyword
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    containers = soup.findAll('div', {'class': 's-item-container'})
    try:
        for container in containers:
            brand_container = container.findAll('span', {'class': 'a-size-small a-color-secondary'})
            brand = brand_container[1].text

            title_container = container.findAll('h2', {'class': 'a-size-medium s-inline s-access-title a-text-normal'})
            title = title_container[0].text

            price_container = container.find('span', {'class': 'a-size-base a-color-base'})
            price = price_container.text

            print('Brand: ' + brand)
            print('Name: ' + title)
            print('Price: ' + price)
            print('-------------------------------------------------------')

    except:
        print("some retarded error, try searching for something else. From what i've checked most of the searches dont work.")


listResults(input('Search for: '))
