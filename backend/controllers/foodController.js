const Food = require("../models/Food");

exports.getFoods = async (req, res) => {
  try {
    const foods = await Food.find({ isAvailable: true });

    res.json({
      success: true,
      data: foods,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to fetch foods",
    });
  }
};

exports.createFood = async (req, res) => {
  try {
    const { name, description, price, category, image } = req.body;

    const food = await Food.create({
      name,
      description,
      price,
      category,
      image,
    });

    res.status(201).json({
      success: true,
      message: "Food item created successfully",
      data: food,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to create food item",
    });
  }
};

exports.updateFood = async (req, res) => {
  try {
    const food = await Food.findByIdAndUpdate(req.params.id, req.body, {
      new: true,
    });

    res.json({
      success: true,
      message: "Food item updated successfully",
      data: food,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to update food item",
    });
};