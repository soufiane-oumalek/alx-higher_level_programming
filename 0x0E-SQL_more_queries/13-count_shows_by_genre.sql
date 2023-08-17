-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT gnr.name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres AS gnr
INNER JOIN tv_show_genres AS v ON gnr.id = v.genre_id
GROUP BY gnr.name
ORDER BY number_of_shows DESC;
