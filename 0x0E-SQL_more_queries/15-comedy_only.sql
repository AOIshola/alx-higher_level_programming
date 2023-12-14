-- Lists all genres of the show Dexter
SELECT tv_shows.title as title
  FROM tv_genres
	LEFT JOIN tv_show_genres
	  ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
	  ON tv_shows.id = tv_show_genres.id
 WHERE tv_genres.name = 'Comedy'

