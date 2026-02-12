




-- SELECT a.id, CASE WHEN COUNT(b.id) > 0 THEN "Inner" ELSE "Leaf" END
(SELECT id, CASE WHEN p_id is NULL THEN "Root" END AS "type"
FROM Tree
WHERE p_id IS NULL

UNION

SELECT a.id, CASE WHEN COUNT(b.id) >= 1 THEN "Inner" ELSE "Leaf" END AS "type"
FROM Tree a 
LEFT JOIN Tree b
On a.id = b.p_id
WHERE a.id <>(SELECT id FROM Tree WHERE p_id is NULL)
GROUP BY a.id)
ORDER BY 1 ASC