# Write your MySQL query statement below
SELECT unique_id, name
FROM Employees e LEFT OUTER JOIN EmployeeUNI u
on e.id = u.id
