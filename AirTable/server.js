const express = require('express');
const axios = require('axios');
require('dotenv').config();

const app = express();
const PORT = 3000;

app.get('/records', async (req, res) => {
  try {
    const response = await axios.get(`https://api.airtable.com/v0/${process.env.AIRTABLE_BASE_ID}/Table1`, {
      headers: {
        Authorization: `Bearer ${process.env.AIRTABLE_API_KEY}`,
      },
    });
    res.json(response.data.records);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(PORT, () => console.log(`Server running on port ${PORT}`));

