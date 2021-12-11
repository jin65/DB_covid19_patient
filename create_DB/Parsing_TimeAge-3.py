import sys
import getpass
import pymysql as mysqldb

userid=input('Username: ')
userpwd=getpass.getpass('password: ')
dbname='TeamProject'

mydb = mysqldb.connect(host='localhost', 
                       user=userid, 
                       passwd=userpwd, 
                       db=dbname)
cursor = mydb.cursor()

fname = 'C:/Users/USER/Desktop/대학교/2학년 2학기/데이타베이스/과제/팀프로젝트/1주차자료/addtional_Timeinfo.csv'

pre_conf = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
pre_dec = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for idx, line in enumerate(open(fname)):
    if not idx:
        continue
    
    tok=line.split(',')
    #print(tok)
    
    agelist = ['0s', '10s', '20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s', '100s']
    
    date = tok[0]

    for i in range(0, 11):
        age = agelist[i]
        
        #count confirmed
        sql = "SELECT * FROM PatientInfo where confirmed_date = '%s' and age = '%s'"%(date, age)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        conf = pre_conf[i] + row_cou
        pre_conf[i] = conf
        
        print(row_cou)
        
        #count deceased
        sql = "SELECT * FROM PatientInfo where deceased_date = '%s' and age = '%s'"%(date, age)
        cursor.execute(sql)
        row_cou = cursor.rowcount
        dec = pre_dec[i] + row_cou
        pre_dec[i] = dec
        
        timeage_vals = "%s, %s, %s, %s"%('"{}"'.format(date), '"{}"'.format(age), conf, dec)
        sql = "INSERT INTO TimeAge VALUES (%s)"%(timeage_vals)
        print(sql)
        try:
            cursor.execute(sql)
            print("[OK] Inserting [%s, %s] to TimeAge"%(date, age))
        except mysqldb.IntegrityError:
            print("[Error] %s, %s already in TimeAge"%(date, age))
        
        mydb.commit()

cursor.close()
print("Done")