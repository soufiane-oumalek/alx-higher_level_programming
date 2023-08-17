-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tvshows.title, tv_show_genres.genres_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show.id ORDER BY tv_shows.title ASC, tv_show_genres.genres_id ASC;
