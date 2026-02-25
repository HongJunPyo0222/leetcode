# Write your MySQL query statement below

# 물건 별 첫 판매 년도 찾기

SELECT product_id, year AS "first_year", quantity, price
FROM Sales
WHERE (product_id, year) IN
(SELECT product_id, MIN(year)
FROM Sales
GROUP BY product_id)