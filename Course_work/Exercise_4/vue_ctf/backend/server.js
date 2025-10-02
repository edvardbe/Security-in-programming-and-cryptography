const express = require('express');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const bcrypt = require('bcrypt');
const cors = require('cors')

const app = express();
app.use(bodyParser.json());
app.use(express.static('public'));
app.use(cors({
  origin: "http://localhost:5173", // your frontend URL
  methods: ["GET", "POST"],
  allowedHeaders: ["Content-Type"]
}));


const pool = new Pool({
    user: 'demo',
    host: 'db',
    database: 'demo',
    password: 'demopw',
    port: 5432,
});


app.post('/api/login', async (req, res) => {
    const { username, password } = req.body || {};
    if (!username || !password) return res.status(400).json({ error: 'Missing fields' });


    try {
        const q = 'SELECT id, username, password_hash FROM users WHERE username = $1';
        const result = await pool.query(q, [username]);
        if (result.rowCount === 0) return res.status(401).json({ error: 'Invalid credentials' });


        const user = result.rows[0];
        const ok = await bcrypt.compare(password, user.password_hash);
        if (!ok) return res.status(401).json({ error: 'Invalid credentials' });

    res.json({ message: 'Login successful', user: { id: user.id, username: user.username } });
    } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Server error' });
    }
});


const port = 3000;
app.listen(port, () => console.log(`Server listening on ${port}`));