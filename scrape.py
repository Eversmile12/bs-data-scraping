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


from sqlalchemy import create_engine, MetaData, Table, select, insert
from bs4 import BeautifulSoup
import requests

engine = create_engine('mysql+pymysql://USERNAME:PASSWORD@HOST/DBNAME')
connection = engine.connect()
metadata = MetaData()

data_table = Table('data-scraping', metadata, autoload=True, autoload_with=engine)


source = requests.get('https://rubberducks.herokuapp.com/').text
soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all("div", class_="article"):
    title = article.find('h2').text
    content = article.find('p').text
    stmt = (
        insert(data_table).
        values(data_title=title, data_content=content)
    )
    connection.execute(stmt)




