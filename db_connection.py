from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, MetaData, Table, select, insert
load_dotenv('.env', verbose = True)

print(os.getenv('DB_USERNAME'))
db_uri = 'mysql+pymysql://{username}:{password}@{db_host}/{db_name}'.format(
    username = os.getenv('DB_USERNAME'),
    password = os.getenv('DB_PASSWORD'),
    db_host = os.getenv('DB_HOST'),
    db_name = os.getenv('DB_NAME')
)
engine = create_engine(db_uri)
connection = engine.connect()
metadata = MetaData()

data_table = Table('data-scraping', metadata, autoload=True, autoload_with=engine)



def addDucks(ducks):
    print(ducks['duck_name'])
    print(ducks['duck_price'])
    print(ducks['duck_image'])
    ins = data_table.insert().values(duck_name = ducks['duck_name'], duck_price=ducks['duck_price'], duck_image=ducks['duck_image'], duck_url=ducks['duck_url'])
    connection.execute(ins)
