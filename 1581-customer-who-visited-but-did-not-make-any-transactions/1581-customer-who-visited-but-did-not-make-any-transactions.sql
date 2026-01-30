# Write your MySQL query statement below
# 환승하지 않고 방문한사람들 ID 찾아내기
-- +----------+-------------+
-- | visit_id | customer_id |
-- +----------+-------------+
-- | 4        | 30          |
-- | 6        | 96          |
-- | 7        | 54          |
-- | 8        | 54          |
-- +----------+-------------+

SELECT customer_id, count(*) as "count_no_trans"
FROM Visits
WHERE visit_id NOT IN(SELECT visit_id FROM Transactions)
GROUP BY customer_id

