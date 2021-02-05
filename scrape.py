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
from db_connection import data_table, connection
import requests


duck_website = 'https://shop.justducks.co.uk/characters-2?limitstart=0?limitstart=0?limitstart=0?limitstart=0&limit=0'
source = requests.get(duck_website).text
soup = BeautifulSoup(source, 'lxml')


main_content = soup.find('div', class_='hikashop_product')
print(main_content)




