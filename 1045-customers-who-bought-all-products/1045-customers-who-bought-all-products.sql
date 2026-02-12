# Write your MySQL query statement below




# 모든 제품을 산 고객 ID를 출력해라

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT(product_key)) = 
(SELECT COUNT(DISTINCT(product_key))
FROM Product
)