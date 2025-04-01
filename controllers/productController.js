const Product = require('../models/Product');

async function listProducts(req, res) {
    try {
        const products = await Product.find({});
        res.json(products);
    } catch (error) {
        console.error('Failed to retrieve products', error);
        res.status(500).send('Failed to get products');
    }
}

module.exports = { listProducts };
