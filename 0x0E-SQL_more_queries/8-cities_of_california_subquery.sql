--  lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM cities WHERE state_id = (SELECT ID FROM state WHERE name = 'California')
ORDER BY id ASC;
