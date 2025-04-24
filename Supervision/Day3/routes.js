// Display form
app.get('/form', (req, res) => {
    res.render('form');
  });
  
  // Handle form submission
  app.post('/add', (req, res) => {
    const { name, age, grade, email, phone, address } = req.body;
    db.query('INSERT INTO students SET ?', { name, age, grade, email, phone, address }, err => {
      if (err) throw err;
      res.redirect('/students');
    });
  });
  
  // Show all students
  app.get('/students', (req, res) => {
    db.query('SELECT * FROM students', (err, results) => {
      if (err) throw err;
      res.render('students', { students: results });
    });
  });
  