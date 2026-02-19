# Write your MySQL query statement below


# 랭크는 내림차순
# 동률은 같은 랭킹

SELECT score, DENSE_RANK() OVER (ORDER BY score DESC) AS "rank"
FROM Scores