const express = require('express');
const app = express();
const port = 3000;

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Sample list of events (This can be modified later)
const events = [
  { name: "Tech Meetup", date: "April 25, 2025", location: "KLab" },
  { name: "Community Cleaning Day", date: "May 1, 2025", location: "Nyamirambo" },
  { name: "Youth Worship Night", date: "May 5, 2025", location: "Amahoro Stadium" }
];

// Route for the homepage
app.get('/', (req, res) => {
  res.render('index', { events });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
