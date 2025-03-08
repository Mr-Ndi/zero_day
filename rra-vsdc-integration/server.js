require('dotenv').config();
const express = require('express');
const morgan = require('morgan')
const axios = require('axios');

const app = express();
app.use(express.json());
app.use(morgan('dev'))

const VSDC_BASE_URL="https://test-vsdc.rra.gov.rw/api/v1/";

app.get('/', (req, res) => {
    res.send('RRA VSDC Integration Server is Running ✅');
});


app.post('/initial', async(requestAnimationFrame, res)=>{
    try {
        const requiredData ={
            tin: "999999999",       // Test TIN
            bhfId: "00",            // Headquarters
            dvcSrlNo: "TEST-DEVICE" // Dummy device serial number
              
        };

        // const response = await axios.post(`${VSDC_BASE_URL}/initializer/selectInitialInfo`, requiredData)
        const response = await axios.post(`${VSDC_BASE_URL}/initializer/selectInitInfo`, requiredData);
        res.json(response.data)
        
    } catch (error) {
        res.status(500).json({ error: error.message })
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, ()=> console.log(`Server running on port ${PORT}`))