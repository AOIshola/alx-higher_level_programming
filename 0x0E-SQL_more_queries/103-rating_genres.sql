-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating
SELECT tv_genres.name AS name, SUM(rate) AS rating
  FROM tv_show_ratings
	JOIN tv_shows
	  ON tv_shows.id = tv_show_ratings.show_id
       RIGHT JOIN tv_show_genres
	  ON tv_shows.id = tv_show_genres.show_id
	JOIN tv_genres
	  ON tv_genres.id = tv_show_genres.genre_id
 GROUP BY name
 ORDER BY rating DESC
