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


fname='C:/Users/USER/Desktop/대학교/2학년 2학기/데이타베이스/과제/팀프로젝트/1주차자료/addtional_Timeinfo.csv'

pre_conf = 0
pre_rel = 0
pre_dec = 0
for ldx, line in enumerate(open(fname)):
	if not ldx:						# skip first line (the header)
		continue

	tok=line.split(',')
	#print(tok)

	date = tok[0]
	test = tok[1]
	neg = tok[2]

	#count confirmed
	sql = "SELECT * FROM PatientInfo where confirmed_date = '%s'"%(date)
	cursor.execute(sql)
	row_cou = cursor.rowcount
	conf = pre_conf + row_cou
	pre_conf = conf

	#count released
	sql = "SELECT * FROM PatientInfo where released_date = '%s'"%(date)
	cursor.execute(sql)
	row_cou = cursor.rowcount
	rel = pre_rel + row_cou
	pre_rel = rel

	#count deceased
	sql = "SELECT * FROM PatientInfo where deceased_date = '%s'"%(date)
	cursor.execute(sql)
	row_cou = cursor.rowcount
	dec = pre_dec + row_cou
	pre_dec = dec

	timeinfo_vals = "%s, %s, %s, %s, %s, %s"%('"{}"'.format(date), test, neg, conf, rel, dec)

	sql = "INSERT INTO TimeInfo VALUES (%s)"%(timeinfo_vals)
	print(sql)
	try:
	    cursor.execute(sql)
	    print("[OK] Inserting [%s] to TimeInfo"%(date))
	except mysqldb.IntegrityError:
		print("[Error] %s already in TimeInfo"%(date))

	mydb.commit()

cursor.close()
print("Done")