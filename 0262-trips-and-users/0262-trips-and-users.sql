# Write your MySQL query statement below

# 밴되지 않은 유저중 20131001 20131013 사이

SELECT t.request_at AS "Day",
ROUNd(COUNT(IF(t.status = 'cancelled_by_client' or t.status = 'cancelled_by_driver' , t.status, NULL))/COUNT(*), 2) AS "Cancellation Rate"
FROM Trips t
LEFT JOIN Users u
ON t.client_id = u.users_id
LEFT JOIN Users d
ON t.driver_id = d.users_id
WHERE u.banned != 'Yes' AND (t.request_at BETWEEN "2013-10-01" AND "2013-10-03") AND (d.banned != 'Yes')
GROUP BY request_at



-- FROM Trips t LEFT JOIN Users u
-- ON t.client_id = u.users_id AND t.driver_id = u.users_id
