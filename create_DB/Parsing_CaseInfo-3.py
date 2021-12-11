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


fname='C:/Users/USER/Desktop/대학교/2학년 2학기/데이타베이스/과제/팀프로젝트/1주차자료/K_COVID19.csv'
for ldx, line in enumerate(open(fname)):
	if not ldx:						# skip first line (the header)
		continue

	tok=line.split(',')
	print(tok)

	cid = tok[17]
	if(tok[18]=='NULL' or tok[18]=='from other city'):
		province = 'NULL'
	else:
		province = tok[4]
	city = tok[18]
	inf_group = tok[19]
	inf_case = tok[6]
	conf = tok[20]
	lati = tok[21]
	longti = tok[22]

	if(city =='NULL'):
		case_vals = "%s, %s, %s, %s, %s, %s, %s, %s"%(cid, province, city, inf_group, '"{}"'.format(inf_case), conf, lati, longti)
	elif(city == 'from other city'):
		case_vals = "%s, %s, %s, %s, %s, %s, %s, %s"%(cid, province, '"{}"'.format(city), inf_group, '"{}"'.format(inf_case), conf, lati, longti)
	else:
		case_vals = "%s, %s, %s, %s, %s, %s, %s, %s"%(cid, '"{}"'.format(province), '"{}"'.format(city), inf_group, '"{}"'.format(inf_case), conf, lati, longti)

	sql = 'INSERT INTO CaseInfo VALUES (%s)'%(case_vals)
	print(sql)
	try:
		cursor.execute(sql);
		print("[OK] Inserting [%s] to PatientInfo"%(cid))
	except mysqldb.IntegrityError:
		print("[Error] %s already in PatientInfo"%(cid))

	mydb.commit()

cursor.close()
print("Done")