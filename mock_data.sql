-- Compare all the addresses in the table and output the ones that are identical under the column name married
SELECT adress, 'Yes' AS married
FROM users
GROUP BY adress
HAVING COUNT(*) > 1;

SELECT adress, 'No' AS married
FROM users
GROUP BY adress
HAVING COUNT(*) = 1;
------------------------------------------------------------------------------------------------------------------------------------------------------



