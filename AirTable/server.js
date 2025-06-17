const express = require('express');
const axios = require('axios');
const morgan = require('morgan');
require('dotenv').config();

const app = express();
const PORT = 3000;

app.use(morgan('dev')); // I can also use 'tiny', 'combined', etc.
app.get('/', (req, res) => {
  res.send('Look fam, Airtable API is running. Visit /records to fetch data.');
});

app.get('/records', async (req, res) => {
  try {
    const response = await axios.get(`https://api.airtable.com/v0/${process.env.AIRTABLE_BASE_ID}/Tasks`, {
      headers: {
        Authorization: `Bearer ${process.env.AIRTABLE_API_KEY}`,
      },
    });

    const records = response.data.records.map((record) => ({
      id: record.id,
      name: record.fields.Name,
      notes: record.fields.Notes || '',
      status: record.fields.Status || 'Not Started',
      assignee: record.fields.Assignee?.[0]?.email || 'Unassigned',
      createdTime: record.createdTime,
    }));

    res.json(records);
  } catch (error) {
    console.error('Error fetching records:', error.response?.data || error.message);
    res.status(500).send('Failed to fetch records');
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});

