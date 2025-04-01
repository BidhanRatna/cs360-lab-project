const express = require('express');
const mongoose = require('mongoose');
const { listProducts } = require('./controllers/productController');

const app = express();
const port = 3001;

// Connect to MongoDB
const mongoURI = 'mongodb://localhost:27017/yourDatabaseName'; // Replace 'yourDatabaseName' with your actual database name
mongoose.connect(mongoURI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log('MongoDB connected successfully'))
  .catch(err => console.log(err));

// Middleware to parse JSON bodies
app.use(express.json());

// Route to handle the root path
app.get('/', (req, res) => {
    res.send('Welcome to the Product API');
});

// Products API route using the controller
app.get('/api/products', listProducts);

// Start the server
app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});

// Handle server shutdown gracefully
process.on('SIGINT', async () => {
    console.log('Closing MongoDB connection');
    if (mongoose.connection.readyState) {
        await mongoose.connection.close();
    }
    console.log('MongoDB connection closed');
    process.exit(0);
});
