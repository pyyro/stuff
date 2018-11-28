"""
this used to work when i wrote this
now it doesnt, atleast on my machine
maybe newegg changed their code of the product containers
or maybe my laptop is retarded now
or maybe im retarded
"""

from bs4 import BeautifulSoup
import requests


def listItems(keyword):
    url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=' + str(keyword) + '&N=-1&isNodeId=1'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'html.parser')
    containers = soup.findAll('div', {'class': 'item-container'})
    try:

        for container in containers:
            brand = container.div.div.a.img['title']

            name_container = container.find('a', {'class': 'item-title'})
            name = name_container.text

            price_cont_finder = container.find('div', {'class': 'item-action'})
            price_container = price_cont_finder.find('strong')
            price = price_container.text

            print('Brand: ' + brand)
            print('Name ' + name)
            print('Price: ' + '$' + price)
            print('================================================')
    except:
        print('some retarded error, code still works.')


print('code author: yahikodark')
listItems(input('Search for: '))

k = input('Press Enter to quit') #forgot why i added this
                                 #probably to have the terminal ask for a input instead of immediately quiting after listing
                                 #the results... idk i forgot 
