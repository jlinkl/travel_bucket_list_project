DROP TABLE visits;
DROP TABLE attractions;
DROP TABLE cities;
DROP TABLE users;
DROP TABLE countries;


-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255)
-- );

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

-- CREATE TABLE attractions (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(255),
--     city_id (INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE)
-- );

-- CREATE TABLE visits (
--     id SERIAL PRIMARY KEY,
--     user_id INT NOT NULL REFERENCES user(id) ON DELETE CASCADE,
--     attraction_id INT NOT NULL REFERENCES attractions(id) ON DELETE CASCADE,
--     review TEXT
-- );