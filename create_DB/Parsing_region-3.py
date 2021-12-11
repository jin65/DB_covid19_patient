#!/usr/bin/env python
import sys
import getpass 
#import MySQLdb as mysqldb
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
origin_data.drop(origin_data.columns[[18,21,22]], axis=True, inplace=True)
#print(origin_data)

region=origin_data[['region_code', 'province', 'city', 'latitude.1', 'longitude.1', 'elementary_school_count', \
    'kindergarten_count', 'university_count', 'academy_ratio', 'elderly_population_ratio', \
        'elderly_alone_ratio', 'nursing_home_count']]

new_region=region.dropna(subset=['region_code'])
new_region=new_region.drop_duplicates()
renew_region=new_region.rename(columns={'latitude.1':'latitude', 'longitude.1':'longitude'})

#print(renew_region)

renew_region.to_sql(name='region', con=db_connection, if_exists='append', index=False)