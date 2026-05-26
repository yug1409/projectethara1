const express = require("express");

const router = express.Router();

const {
  getFoods,
  getFoodById,
  createFood,
  updateFood,
  deleteFood,
} = require("../controllers/foodController");

const { protect } = require("../middleware/authMiddleware");

const adminOnly = require("../middleware/adminMiddleware");

// Public Routes
router.get("/", getFoods);

router.get("/:id", getFoodById);

// Admin Routes
router.post("/", protect, adminOnly, createFood);

router.put("/:id", protect, adminOnly, updateFood);

router.delete("/:id", protect, adminOnly, deleteFood);

module.exports = router;
