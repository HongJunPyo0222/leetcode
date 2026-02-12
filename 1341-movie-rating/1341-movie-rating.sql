# Write your MySQL query statement below


# 영화별 가장 큰 별점을 준사람 찾기
# 2020월 2월의 가장 높은 평균찾기

(SELECT u.name AS "results"
FROM Users u LEFT JOIN MovieRating mr
ON u.user_id = mr.user_id
GROUP BY u.user_id
ORDER BY COUNT(mr.rating) DESC, u.name ASC
LIMIT 1)

UNION ALL

(SELECT m.title AS "results"
FROM Movies m LEFT JOIN MovieRating mr
ON m.movie_id = mr.movie_id
WHERE YEAR(mr.created_at) = "2020" AND MONTH(mr.created_at) = "2"
GROUP BY m.movie_id
ORDER BY AVG(mr.rating) DESC, m.title ASC 
LIMIT 1)

-- SELECT movie_id
-- FROM MovieRating
-- WHERE YEAR(created_at) = "2020" AND MONTH(created_at) = "2"
-- GROUP BY movie_id
