const express = require('express');
const mysql = require('mysql');
const bodyParser = require('body-parser');

const app = express();
app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const database = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: '',
    database: 'mydatabase'
});

database.connect((err) => {
    if (err) {
        console.log(`Internal Server Error: ${err}`);
        return;
    } else {
        console.log('Database connected successfully');
    }
});

app.get('/', (req, resp) => {
    resp.render('form');
});

// POST route for creating a new student
app.post('/student', (req, resp) => {
    const { name, age, grade, email, phone, address } = req.body;

    const sql = `INSERT INTO student (name, age, grade, email, phone, address) VALUES (?, ?, ?, ?, ?, ?)`;

    database.query(sql, [name, age, grade, email, phone, address], (err) => {
        if (err) {
            resp.status(500).send(`Student not added: ${err}`);
        } else {
            resp.redirect('/');
        }
    });
});

// GET route to display all students
app.get('/table', (req, resp) => {
    const sql = `SELECT * FROM student`;
    database.query(sql, (err, results) => {
        if (err) {
            resp.status(500).send(`Failed to retrieve data: ${err}`);
        } else {
            resp.render('table', { results });
        }
    });
});

// GET route to delete a student
app.get('/delete/:delete_id', (req, resp) => {
    const { delete_id } = req.params;
    const sql = `DELETE FROM student WHERE id = ?`;

    database.query(sql, [delete_id], (err) => {
        if (err) {
            resp.status(500).send(`Delete failed: ${err}`);
        } else {
            resp.redirect('/table');
        }
    });
});

// GET route to show the update form
app.get('/update/:id', (req, resp) => {
    const { id } = req.params;
    const sql = `SELECT * FROM student WHERE id = ?`;

    database.query(sql, [id], (err, result) => {
        if (err) {
            resp.status(500).send(`Failed to fetch student: ${err}`);
        } else {
            resp.render('updateform', { student: result[0] });
        }
    });
});

// POST route to update a student's information
app.post('/update/:id', (req, resp) => {
    const { id } = req.params;
    const { name, age, grade, email, phone, address } = req.body;

    const sql = `UPDATE student SET name = ?, age = ?, grade = ?, email = ?, phone = ?, address = ? WHERE id = ?`;

    database.query(sql, [name, age, grade, email, phone, address, id], (err) => {
         if (err) {
            resp.status(500).send(`Update failed: ${err}`);
         } else {
             resp.redirect('/table');
         }
    });
});







app.post('/upate/:id', (req,res) =>{
    const { id } = req.params;
    const {name,age,grade,email,phone,address} = req.body;
    
    const sql = `UPDATE STUDENT SET NAME =?, AGE=?,GRADE=?,EMAIL=?,PHONE=?.ADDRESS=? WHERE id=?`
    database.query(sql, [name,age, grade,email,phone,address, id], (err)=>{
        if(err){
            res.status(500).send(`Updating the database has failed ${err}`)
        }
        else{
            res.redirect('/ta')
        }
    })
})













































app.listen(5000, () => {
    console.log('Server running on http://localhost:5000');
});













