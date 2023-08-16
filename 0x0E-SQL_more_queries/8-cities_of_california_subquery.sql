-- Lists all the cities of California
SET @california_state_id = (SELECT id FROM states WHERE name = 'California');
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id, name ASC;
