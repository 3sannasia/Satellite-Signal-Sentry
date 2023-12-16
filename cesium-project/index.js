const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const { result } = require('lodash');
    
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, '/frontend'))); 

app.use(bodyParser.urlencoded({extended:true}));

app.get('/', (req, res) => {
    res.send("Hello World"); // This will display "Hello World" on the page
    res.sendFile(path.join(__dirname, 'frontend', 'map.html'));
    console.log("GET request to the root");
});

app.listen(3001, () => {
    console.log('Server is running on http://localhost:3001/');
});

// console.log("WILL IT PRINT?");