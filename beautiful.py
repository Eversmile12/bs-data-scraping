from bs4 import BeautifulSoup
import requests
import time
import random
import argparse


parser = argparse.ArgumentParser(description= "Scrape internships data")
parser.add_argument("--dev", dest='feature', action="store_false")
parser.set_defaults(feature=True)
args = parser.parse_args()

def createSoup(url):
    try:
        if args.feature:
            random_sleep = random.randrange(2,7)
            print("sleeping for {random_sleep} seconds".format(random_sleep = random_sleep))
            time.sleep(random_sleep)
        source = requests.get(url).text
        soup = BeautifulSoup(source,'lxml')
        return soup
    except:
        return None