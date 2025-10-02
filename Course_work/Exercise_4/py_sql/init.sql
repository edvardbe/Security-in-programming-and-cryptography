CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    flag TEXT
);

INSERT INTO users (username, password, flag) VALUES
('admin', 'admin123', 'FLAG{MiBombaclat}')
WHERE NOT EXISTS (SELECT 1 FROM users WHERE username='admin');
