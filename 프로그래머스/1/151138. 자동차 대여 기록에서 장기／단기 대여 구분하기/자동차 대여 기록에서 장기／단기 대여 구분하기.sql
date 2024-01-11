SELECT
history_id,
car_id,
DATE_FORMAT(start_date, '%Y-%m-%d') as start_date,
DATE_FORMAT(end_date, '%Y-%m-%d') as end_date,
CASE 
    WHEN (DATEDIFF(end_date, start_date)+1) >= 30 THEN '장기 대여'
    ELSE '단기 대여' END
    AS RENT_TYPE
FROM 
    car_rental_company_rental_history
where START_DATE like '2022-09%'
order by HISTORY_ID desc