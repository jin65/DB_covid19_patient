#!/usr/bin/env python
import sys
import getpass
import pymysql as mysqldb
import pandas as pd

#userid=input('Username: ')
#userpwd=getpass.getpass('Password: ')
#dbname='team_project'
#host='localhost'

#db_connection_str='mysql+pymysql://'+userid+':'+userpwd+'@'+host+'/'+dbname
#db_connection=create_engine(db_connection_str)
#conn=db_connection.connect()

import sys
import getpass
import pymysql as mysqldb

userid='root'
userpwd='2019110124'
dbname='team_project'

mydb = mysqldb.connect(host='localhost', 
                       user=userid, 
                       passwd=userpwd, 
                       db=dbname)
cursor = mydb.cursor()

fname = 'C:\Users\admin\Desktop\addtional_Timeinfo.csv'

pre_conf = [0, 0]
pre_dec = [0, 0]

for idx, line in enumerate(open(fname)):
    if not idx:
        continue
    
    tok=line.split(',')
    #print(tok)
    
    genderlist = ['male', 'female']
    
    date = tok[0]

    for i in range(0, 2):
        gender = genderlist[i]
        
        #count confirmed
        sql = "SELECT * FROM PatientInfo where confirmed_date = '%s' and sex = '%s'"%(date, gender)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        conf = pre_conf[i] + row_cou
        pre_conf[i] = conf
        
        print(row_cou)
        
        #count deceased
        sql = "SELECT * FROM PatientInfo where deceased_date = '%s' and sex = '%s'"%(date, gender)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        dec = pre_dec[i] + row_cou
        pre_dec[i] = dec
        
        timegender_vals = "%s, %s, %s, %s"%('"{}"'.format(date), '"{}"'.format(gender), conf, dec)
        sql = "INSERT INTO TimeGender VALUES (%s)"%(timegender_vals)
        print(sql)
        try:
            cursor.execute(sql)
            print("[OK] Inserting [%s, %s] to TimeGender"%(date, gender))
        except mysqldb.IntegrityError:
            print("[Error] %s, %s already in TimeGender"%(date, gender))
        
        mydb.commit()

cursor.close()
print("Done")