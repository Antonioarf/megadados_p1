from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
import mysql.connector
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# Database parameter
with open('dados.json') as json_file:
    data = json.load(json_file)

host = data['host']         
user = data['user']          
passwd = data['passwd']    
database = "api"     

# Database connection
#db= mysql.connector.connect(
#        host='localhost',
#        user='root',
#        password='Fonseca01',
#        database='api')

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="Fonseca01"
#)

#mycursor = mydb.cursor()
#mycursor.execute("DROP DATABASE IF EXISTS api; CREATE DATABASE api;")

engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')
#cursor=db.cursor()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()