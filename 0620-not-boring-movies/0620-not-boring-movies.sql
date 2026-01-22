# Write your MySQL query statement below

#홀수 ID, description != boring, 레이팅 내림차순

SELECT *
FROM Cinema
WHERE id % 2 = 1 and description != "boring"
ORDER BY rating DESC