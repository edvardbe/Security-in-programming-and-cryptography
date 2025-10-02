CREATE TABLE IF NOT EXISTS users (
id SERIAL PRIMARY KEY,
username TEXT UNIQUE NOT NULL,
password_hash TEXT NOT NULL
);


INSERT INTO users (username, password_hash)
VALUES 
('admin', '$2a$12$nCtcKh.ZUyyYAJkzO7h4ouoMggbIrzHK8x1fDJcZBq5G2hUY9vcB2'),
('evil', '$2a$12$K7MTq/zWh645LS4RdvZ6J.fNpF4yk0VDAQmjvFXkKWLsRDy5C83Pq');
