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

	pid = tok[0]
	if(tok[1] == "NULL"):
		sex = "UNKNOWN"
	else:
		sex = tok[1]
	if(tok[2] == "NULL"):
		age = "UNKNOWN"
	else:
		age = tok[2]
	country = tok[3]
	if(tok[4]=="NULL"):
		province = "UNKNOWN"
	else:
		province = tok[4]
	city = tok[5]
	if(tok[6]=="NULL"):
                	inf_case = "UNKNOWN"
	else:
		inf_case = tok[6]
	inf_by = tok[7]
	con_num = tok[8]

	if(tok[9] == "NULL"):
		symptom_date = "1000-01-01"
	else:
		symptom_date = tok[9]
	if(tok[10] == "NULL"):
		conf_date = "1000-01-01"
	else:
		conf_date = tok[10]
	if(tok[11]=="NULL"):
		rel_date = "1000-01-01"
	else:
		rel_date = tok[11]
	if(tok[12] =="NULL"):
		dec_date = "1000-01-01"
	else:
		dec_date = tok[12]
	state = tok[13]

	if(city == "NULL"):
		patient_vals = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s"%(pid, '"{}"'.format(sex), '"{}"'.format(age), '"{}"'.format(country), '"{}"'.format(province), city, '"{}"'.format(inf_case), inf_by, con_num, '"{}"'.format(symptom_date), '"{}"'.format(conf_date), '"{}"'.format(rel_date), '"{}"'.format(dec_date), '"{}"'.format(state))
	else:
		patient_vals = "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s"%(pid, '"{}"'.format(sex), '"{}"'.format(age), '"{}"'.format(country), '"{}"'.format(province), '"{}"'.format(city), '"{}"'.format(inf_case), inf_by, con_num, '"{}"'.format(symptom_date), '"{}"'.format(conf_date), '"{}"'.format(rel_date), '"{}"'.format(dec_date), '"{}"'.format(state))

	sql = 'INSERT INTO PatientInfo VALUES (%s)'%(patient_vals)
	print(sql)
	try:
	    cursor.execute(sql);
	    print("[OK] Inserting [%s] to PatientInfo"%(pid))
	except mysqldb.IntegrityError:
		print("[Error] %s already in PatientInfo"%(pid))

	mydb.commit()

cursor.close()
print("Done")
