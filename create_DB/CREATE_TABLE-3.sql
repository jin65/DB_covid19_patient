CREATE TABLE PatientInfo(
patient_id bigint NOT NULL,
sex varchar(10),
age varchar(10),
country varchar(50),
province varchar(50),
city varchar(50),
infection_case varchar(50),
infected_by bigint,
contact_number int,
symptom_onset_date date,
confirmed_date date,
released_date date,
deceased_date date,
state varchar(20),
PRIMARY KEY(patient_id, sex, age, province, infection_case, confirmed_date),
INDEX idx_sex(sex),
INDEX idx_age(age),
INDEX idx_province(province),
INDEX idx_infectioncase(infection_case),
INDEX idx_confirmed_date(confirmed_date));

-- ALTER TABLE PatientInfo add FOREIGN KEY(infected_by) REFERENCES PatientInfo(patient_id);

CREATE TABLE CaseInfo(
case_id int NOT NULL,
province varchar(50),
city varchar(50),
infection_group tinyint(1),
infection_case varchar(50),
confirmed int,
latitude float,
longtitude float,
PRIMARY KEY(case_id));

-- ALTER TABLE CaseInfo add FOREIGN KEY(infection_case) REFERENCES PatientInfo(infection_case);

CREATE TABLE Region(
region_code int NOT NULL,
province varchar(50),
city varchar(50),
latitude float,
longtitude float,
elementary_school_count int,
kindergarten_count int,
university_count int,
academy_ratio float,
elderly_population_ratio float,
elderly_alone_ratio float,
nursing_home_count int,
PRIMARY KEY(region_code));

-- ALTER TABLE Region add FOREIGN KEY(province) REFERENCES PatientInfo(province);

CREATE TABLE Weather(
region_code int NOT NULL,
province varchar(50),
wdate date NOT NULL,
avg_temp float,
min_temp float,
max_temp float,
PRIMARY KEY(region_code, wdate));

-- ALTER TABLE Weather add FOREIGN KEY(wdate) REFERENCES PatientInfo(confirmed_date);

CREATE TABLE TimeInfo(
date date NOT NULL,
test int(11),
negative int(11),
confirmed int(11),
released int(11),
deceased int(11),
PRIMARY KEY (date));

-- ALTER TABLE TimeInfo add FOREIGN KEY(date) REFERENCES PatientInfo(confirmed_date);

CREATE TABLE TimeAge(
date date NOT NULL,
age varchar(10) NOT NULL,
confirmed int(11),
deceased int(11),
PRIMARY KEY (date, age));

-- ALTER TABLE TimeAge add FOREIGN KEY(date) REFERENCES TimeInfo(date);
-- ALTER TABLE TimeAge add FOREIGN KEY(age) REFERENCES PatientInfo(age);

CREATE TABLE TimeGender(
date date NOT NULL,
sex varchar(10) NOT NULL,
confirmed int(11),
deceased int(11),
PRIMARY KEY (date, sex));

-- ALTER TABLE TimeGender add FOREIGN KEY(date) REFERENCES TimeInfo(date);
-- ALTER TABLE TimeGender add FOREIGN KEY(sex) REFERENCES PatientInfo(sex);

CREATE TABLE TimeProvince(
date date NOT NULL,
province varchar(50) NOT NULL,
confirmed int(11),
released int(11),
deceasesd int(11),
PRIMARY KEY (date, province));

-- ALTER TABLE TimeProvince add FOREIGN KEY(date) REFERENCES TimeInfo(date);
-- ALTER TABLE TimeProvince add FOREIGN KEY(province) REFERENCES PatientInfo(province);