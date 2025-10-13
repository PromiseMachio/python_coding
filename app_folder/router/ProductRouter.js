const express = require('express');
const router = express.Router();
const product = require('../models/products');

// Introducing the CRUD operation
// Searching 
router.get("/", async (req, res) =>{
    try {
        const Product = await product.find();
        res.json(Product);
    } catch (error) {
        res.status(500).json({message:error.message})
    }
});
// Create the schema tables in express
router.post("/", async(req,res)=>{
    const {id, name, description, price, cartegory, instock} = req.body;
    try {
        const Product = new product({id, name, description, price, cartegory, instock});
        const saved = await Product.save();
        res.status(201).json(saved)
    } catch (error) {
        res.status(401).json({message:error.message});
    }
});
// Update by ID 
router.put("/:id", async(req, res) => {
    try {
        const Product = await product.findByIdAndUpdate(
            req.params.id,
            req.body,
            {new:true}
        );
        res.json(Product)
    } catch (error) {
        res.status(400).json({message:error.message})
    }
});

// Delete by Id
router.delete("/:id", async(req, res)=>{
    try {
        await product.findByIdAndDelete(
            req.params.id
        );
        res.json({message:"Deleted succesfully..."});
    } catch (error) {
        res.status(500).json({message:error.message})
    }
});

module.exports= router;