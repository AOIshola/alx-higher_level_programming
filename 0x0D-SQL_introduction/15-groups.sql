-- Lists all records with the same score
SELECT `score`, COUNT(`name`) 'number' FROM second_table GROUP BY `score`
ORDER BY 'number' DESC
