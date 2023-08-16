-- Create table unique_id with a unique id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL,
    name VARCHAR(256),
    PRIMARY KEY (id),
    UNIQUE (id)
);
