-- Lists all the cities of California
SELECT id FROM states WHERE name = 'California'
SELECT * FROM cities WHERE state_id = @california_state_id ORDER BY id ASC;
