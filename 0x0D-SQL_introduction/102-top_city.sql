-- Displays the top 3 city temp in July and uAgust(Fahrenheit) by city
-- ordered by temperature
SELECT city, AVG(value) avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY avg_temp DESC
LIMIT 3
