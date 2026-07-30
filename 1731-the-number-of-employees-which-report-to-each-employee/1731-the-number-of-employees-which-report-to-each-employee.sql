# Write your MySQL query statement below

#SELECT s.employee_id, avg(s.age)
SELECT s.employee_id, s.name, COUNT(f.reports_to) AS "reports_count", ROUND(AVG(f.age)) AS "average_age"
FROM Employees f JOIN Employees s
ON f.reports_to = s.employee_id
WHERE s.employee_id in (SELECT reports_to FROM Employees)
GROUP BY f.reports_to
ORDER BY 1 ASC