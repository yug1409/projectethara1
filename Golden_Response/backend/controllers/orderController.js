const Order = require("../models/Order");

exports.createOrder = async (req, res) => {
  try {
    const { items, totalAmount, deliveryAddress, phone, paymentMethod } =
      req.body;

    if (!items || items.length === 0) {
      return res.status(400).json({
        success: false,
        message: "Cart is empty",
      });
    }

    const order = await Order.create({
      user: req.user._id,
      items,
      totalAmount,
      deliveryAddress,
      phone,
      paymentMethod,
    });

    res.status(201).json({
      success: true,
      message: "Order placed successfully",
      data: order,
    });
  } catch (error) {
    res.status(500).json({
      success: false,
      message: "Failed to place order",
    });
  }
};

    res.json