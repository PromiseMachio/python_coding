// Clling all the necessary files to be connected for dev to run
const express = require('express');
const dotenv = require('dotenv');
const connectDB = require('./config/connect');


dotenv.config();// Calling the functions in dotenv files
const myApp = express();
// Enable JSON body parsing (middleware for reading POST/PUT body data)
myApp.use(express.json());
//Creating middleware
// routers
myApp.use("/Product", require("./router/ProductRouter"));

//connect DB
connectDB();

// Creating main Homepage
myApp.get("/", (req, res) =>{
    res.send("API is connected  up and running... ")
});

// Starting the server
const PORT = process.env.PORT||5000;
myApp.listen(PORT, () => console.log(`server running in http://localhost:${PORT}`));


