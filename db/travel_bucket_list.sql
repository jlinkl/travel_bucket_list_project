DROP TABLE visits;
DROP TABLE attractions;
DROP TABLE cities;
DROP TABLE countries;

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE attractions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE
);

CREATE TABLE visits (
    id SERIAL PRIMARY KEY,
    attraction_id INT NOT NULL REFERENCES attractions(id) ON DELETE CASCADE,
    visited BOOLEAN,
    wants_to_visit BOOLEAN
);