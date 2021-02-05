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
