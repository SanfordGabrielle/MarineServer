DROP TABLE IF EXISTS species;

CREATE TABLE species (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    genus TEXT NOT NULL,
    max_age INTEGER NOT NULL,
    region TEXT NOT NULL,
    average_size INTEGER NOT NULL
);

