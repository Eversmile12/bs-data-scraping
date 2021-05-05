from sqlalchemy import create_engine, Table, MetaData, insert, select, text, and_
from sqlalchemy.sql.expression import exists
from dotenv import load_dotenv
import os

load_dotenv('.env')

db_uri = "mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}".format(
    username = os.getenv('DB_USERNAME'),
    password = os.getenv('DB_PASSWORD'),
    host = os.getenv('DB_HOST'),
    dbname = os.getenv('DB_NAME'),
    port = os.getenv('DB_PORT')
)



engine = create_engine(db_uri)
connection = engine.connect()
print("Connecting to AWS RDS...")
metadata = MetaData()
jobs_table = Table('jobsraw', metadata, autoload = True, autoload_with=engine)
print("Connection succeeded!")
# isInDB = jobs_table.select().where(jobs_table.columns.job_id == )
# isInDb = exists(isInDB).select()
# result = connection.execute(isInDB).fetchall()


# jobs = jobs_table.select(['*'])



def addJobs(job_list):
    for job in job_list:
        stmt = jobs_table.select().where(and_(jobs_table.columns.job_title == job["job_title"], jobs_table.columns.job_location == job["job_location"] ))
        stmt = exists(stmt).select()
        result = connection.execute(stmt).scalar()
        if(result):
            print("WARNING: entry is duplicated")
        else:
            print("SUCCEEDED: entry added" )
            stmt = jobs_table.insert()
            result = connection.execute(stmt, job)
    # print(job_list)
    # stmt = select([jobs_table])
    # stmt = insert(jobs_table)
    # result = connection.execute(stmt, job_list)
    # if result.rowcount:
    #     return True
    # else:
    #     return False




# prints 
# print(jobs)
# prints columns name
# print(jobs[0].keys())

