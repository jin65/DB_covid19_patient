-----------------------README FILE-----------------------------

1. 원본 데이터에 city, longitude, latitude 열이 두개씩 있음.
두개의 city 중 앞은 patientInfo를 나타내고 뒷부분은 case정보를 나타낸다.
두개의 longitude/latitude 중 앞은 case의 지역정보, 뒷부분은 환자거주지역의 위도 및 경도를 나타낸다. 
region테이블은 city1, longitude2, latitude2를 사용했고
case 테이블은 city2, longitude1, latitude1을 사용했다.

2. weather table
region_code와 wdate(confirmed_date)가 모두 null 인 행 존재함:: pandas의 dropna함수로 제외했다.

3. region table
region_code가 null인 행 존재:: dropna함수로 해당 튜플은 제외시킴

4. PatientInfo
sex, age, province, infection_case, confirmed_date
위 5개는 다른 테이블에 의해 참조되므로 NULL 값이 있으면 안된다. 따라서 NULL인 경우 'UNKNOWN'으로 대체했고, confirmed_date의 경우 '1000-01-01'로 대체했다.

5. 테이블에 데이터를 삽입할 때 IntegrityError: (1452, ..가 발생하는 경우가 있다,(ex: PatientInfo, TimeInfo..etc) 외래키때문에 발생하는 문제로, 데이터 삽입 후에 alter문을 이용해 외래키를 추가했다.
