//Schema creator
const mongoose = require('mongoose');

const productSchema = new mongoose.Schema({
    id: {type:Number, required:true, unique:true},
    name:{type:String, required:true},
    description:{type:String, required:true},
    price:{type:Number,required:true},
    cartegory:{type:String, required:true},
    instock:{type:Boolean,required:true}
},{timestamps:true});

const product = mongoose.model('product', productSchema);
module.exports = product;