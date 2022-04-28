DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS league;
DROP TABLE IF EXISTS teams;




CREATE TABLE teams (
    id serial PRIMARY KEY,
    name text NOT NULL
);

CREATE TABLE matches (
    id serial PRIMARY KEY,
    home_team_id INT REFERENCES teams(id) ,
    away_team_id INT REFERENCES teams(id),
    home_score INT,
    away_score INT 
);

CREATE TABLE league (
    id serial PRIMARY KEY,
    position INT DEFAULT 1,
    team_id INT REFERENCES teams(id) ,
    points INT
)