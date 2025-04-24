const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');
const app = express();
const port =3000

app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({ extended: true }));

const db = mysql.createConnection({
  host: 'localhost',
  user: 'Ninshuti',
  password: 'byasana',
  database: 'student_management'
});

db.connect(err => {
  if (err) throw err;
  console.log('Connected to MySQL');
});

app.listen(port, () => {
  console.log('----------------------------------------------------');
  console.log(`🚀 Server is running on http://localhost:${port}`);
  console.log('----------------------------------------------------');
});