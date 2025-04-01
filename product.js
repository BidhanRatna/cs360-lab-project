const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  price: Number,
  categories: [String],
  images: [String],
  stock: Number,
  brand: String,
  ratings: {
    average: Number,
    numberOfReviews: Number
  },
  createdAt: Date,
  updatedAt: Date
});

const Product = mongoose.model('Product', productSchema);

module.exports = Product;
