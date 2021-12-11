#!/usr/bin/env python
import sys
import getpass
import pymysql as mysqldb
import pandas as pd

userid='root'
userpwd='2019110124'
dbname='team_project'

mydb = mysqldb.connect(host='localhost', 
                       user=userid, 
                       passwd=userpwd, 
                       db=dbname)
cursor = mydb.cursor()

fname = 'C:\Users\admin\Desktop\addtional_Timeinfo.csv'

data=pd.read_csv("K_COVID19.csv")
province_df=data['province']
province_df=province_df.drop_duplicates()
provinceList=province_df.tolist()
len_province=len(provinceList)


pre_conf = [0 for i in range(len_province)]
pre_rel = [0 for i in range(len_province)]
pre_dec = [0 for i in range(len_province)]

for idx, line in enumerate(open(fname)):
    if not idx:
        continue
    
    tok=line.split(',')
    #print(tok)
    
    date = tok[0]

    for i in range(len_province):
        province = provinceList[i]
        
        #count confirmed
        sql = "SELECT * FROM PatientInfo where confirmed_date = '%s' and province = '%s'"%(date, province)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        conf = pre_conf[i] + row_cou
        pre_conf[i] = conf
        
        print(row_cou)

        #count released
        sql = "SELECT * FROM PatientInfo where released_date = '%s' and province = '%s'"%(date, province)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        rel = pre_rel + row_cou
        pre_rel[i] = rel
        
        #count deceased
        sql = "SELECT * FROM PatientInfo where deceased_date = '%s' and province = '%s'"%(date, province)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        dec = pre_dec[i] + row_cou
        pre_dec[i] = dec
        
        timeprovince_vals = "%s, %s, %s, %s, %s"%('"{}"'.format(date), '"{}"'.format(province), conf, rel, dec)
        sql = "INSERT INTO TimeProvince VALUES (%s)"%(timeprovince_vals)
        print(sql)
        try:
            cursor.execute(sql)
            print("[OK] Inserting [%s, %s] to TimeProvince"%(date, province))
        except mysqldb.IntegrityError:
            print("[Error] %s, %s already in TimeProvince"%(date, province))
        
        mydb.commit()

cursor.close()
print("Done")