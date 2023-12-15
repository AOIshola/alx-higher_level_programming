-- List all genres not linked to the show 'Dexter'
-- CREATE TEMPORARY TABLE IF NOT EXISTS dexter_genres
SELECT name
  FROM tv_genres
 WHERE name NOT IN (
	SELECT tv_genres.name AS name
	  FROM tv_genres
		LEFT JOIN tv_show_genres
		  ON tv_genres.id = tv_show_genres.genre_id
		JOIN tv_shows
		  ON tv_shows.id = tv_show_genres.show_id
	 WHERE tv_shows.title = 'Dexter'
)
 ORDER BY name
