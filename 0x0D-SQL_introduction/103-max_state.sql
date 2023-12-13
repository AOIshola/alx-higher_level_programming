-- Displays the max temperature (Fahrenheit) of each state
-- ordered by state name
SELECT state, MAX(value) max_temp FROM temperatures GROUP BY state ORDER BY state
