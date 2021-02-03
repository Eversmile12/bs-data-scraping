from bs4 import BeautifulSoup
import requests 


with open('simple.html', 'r') as html_file: #<--- opens a file and creates a variable using the specified "as" value
    print (html_file.read())