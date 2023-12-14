-- Lists all shows contained in hbtn_0d_tvshows that have
-- at least one genre linked
SELECT tv_shows.title as title, tv_genres.name as name
  FROM tv_shows
	LEFT JOIN tv_show_genres
	  ON tv_shows.id = tv_show_genres.show_id
	LEFT JOIN tv_genres
	  ON tv_genres.id = tv_show_genres.genre_id
 ORDER BY title, name
