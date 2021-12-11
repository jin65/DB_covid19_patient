#!/usr/bin/env python
import sys
import getpass 
# import MySQLdb as mysqldb
import pymysql as mysqldb
import pandas as pd
from sqlalchemy import create_engine

userid=input('Username: ')
userpwd=getpass.getpass('Password: ')
dbname='team_project'
host='localhost'

# connect to MySQL server
#mydb = mysqldb.connect(host='localhost',
#	user=userid,
#	passwd=userpwd,
#	db=dbname)
#cursor = mydb.cursor()

db_connection_str='mysql+pymysql://'+userid+':'+userpwd+'@'+host+'/'+dbname
db_connection=create_engine(db_connection_str)
conn=db_connection.connect()

origin_data=pd.read_csv("K_COVID19.csv")
#print(origin_data)

weather=origin_data[['region_code', 'province', 'confirmed_date', 'avg_temp', 'min_temp', 'max_temp', ]]
#print(weather)

new_weather=weather.dropna(subset=['region_code'])
#print(new_weather[new_weather['region_code'].isnull()])
#print(new_weather[new_weather['confirmed_date'].isnull()])
new_weather=new_weather.dropna(subset=['confirmed_date'])
#print(new_weather)

new_weather=new_weather.drop_duplicates()
renew_weather=new_weather.rename(columns={'confirmed_date':'wdate'})
#print(renew_weather)

renew_weather.to_sql(name='weather', con=db_connection, if_exists='append', index=False)
