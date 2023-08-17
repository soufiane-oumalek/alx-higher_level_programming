-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT gnr.name FROM tv_genres
INNER JOIN tv_show_genres
ON gnr.id = show.genre_id
INNER JOIN tv_shows
ON tv.id = show.show_id
WHERE tv.title = "Dexter"
ORDER BY gnr.name;
