# Write your MySQL query statement below



# 2016년의 총 투자액을 각 pid에 대해 쓰시오
# 위경도가 중첩되면 안댐
# tiv15가 여러개여야함

SELECT ROUND(SUM(tiv_2016), 2) AS "tiv_2016"
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015 
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) >= 2
    )
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) <=1
)