# from bs4 import BeautifulSoup
# import requests 

# # open value are: w(write),r(read),a(append)
# with open('simple.html', 'r') as html_file: #<--- opens a file and creates a variable using the specified "as" value
#     soup = BeautifulSoup(html_file, 'lxml')

# #print(soup.prettify()); # prettiefies html file.

# first_paragraph= soup.body.div.p #we can retrieve tags accessing them as soup's attributes
# print(first_paragraph)

# header = soup.find('h1') # or using the find method
# print(header)

# article_paragraph_one = soup.find("p", class_="paragraph-article-1") # also specifying the class, the id, or whatever
# print(article_paragraph_one)


from bs4 import BeautifulSoup
from db_connection import data_table, connection, addDucks
import requests


duck_website = 'https://shop.justducks.co.uk/characters-2?limitstart=0?limitstart=0?limitstart=0?limitstart=0&limit=0?limitstart=0?limitstart=0?limitstart=0?limitstart=0&limit=0?limitstart=0?limitstart=0?limitstart=0?limitstart=0&limit=0?limitstart=0?limitstart=0?limitstart=0?limitstart=0&limit=0'
source = requests.get(duck_website).text
soup = BeautifulSoup(source, 'lxml')
duck_shop_entry = 'https://shop.justducks.co.uk'

for duck in soup.find_all('div', class_='hikashop_product'):
    try:
        duck_image = duck.find('picture').img['src']
        duck_image = '{duck_shop_url}{duck_image}'.format(duck_shop_url = duck_shop_entry , duck_image=duck_image)
        # print(duck_image)
        duck_price = duck.find('span', class_="hikashop_product_price").text
        duck_price = duck_price.split(' ')[1]

        duck_meta = duck.find('span', class_='hikashop_product_name').a
        duck_name = duck_meta.text.strip()
        duck_url = '{duck_shop_url}{duck_url}'.format(duck_shop_url=duck_shop_entry, duck_url=duck_meta['href'])
        ducks = {
            'duck_name':duck_name,
            'duck_price':duck_price,
            'duck_image':duck_image,
            'duck_url':duck_url
        }
        print(duck_price)
        addDucks(ducks)
    except:
        pass




