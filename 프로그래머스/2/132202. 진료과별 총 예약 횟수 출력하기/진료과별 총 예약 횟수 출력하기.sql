-- 코드를 입력하세요
SELECT MCDP_CD as 진료과코드, count(*) as 월예약건수
from APPOINTMENT
where MONTH(APNT_YMD) = 5
group by MCDP_CD
order by count(*) asc, MCDP_CD asc
