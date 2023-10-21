-- 코드를 입력하세요
SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o on i.animal_id = o.animal_id
where i.DATETIME > o.DATETIME
order by i.DATETIME asc