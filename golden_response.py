"""
goldenn_response.py



This file contains the complete reference implementation
of the MERN Food Order Management project.

Run:
python goldenn_response.py
"""

import os

# =============================================================================
# WORKSPACE FILES
# =============================================================================

WORKSPACE_FILES = {

    # =========================================================================
    # BACKEND
    # =========================================================================

    "backend/package.json": """
{
  "name": "backend",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node server.js",
    "dev": "nodemon server.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "dependencies": {
    "bcryptjs": "^3.0.3",
    "cors": "^2.8.6",
    "dotenv": "^17.4.2",
    "express": "^5.2.1",
    "express-rate-limit": "^8.5.2",
    "jsonwebtoken": "^9.0.3",
    "mongoose": "^9.6.2"
  },
  "devDependencies": {
    "nodemon": "^3.1.14"
  }
}

""",

  

    "backend/server.js": """
const express = require("express");
const dotenv = require("dotenv");
const cors = require("cors");
const rateLimit = require("express-rate-limit");

const connectDB = require("./config/db");

const authRoutes = require("./routes/authRoutes");
const foodRoutes = require("./routes/foodRoutes");
const orderRoutes = require("./routes/orderRoutes");

dotenv.config();

connectDB();

const app = express();

app.use(express.json());
app.use(cors());

const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000,
  max: 5,
  message: {
    success: false,
    message: "Too many login attempts. Please try again later.",
  },
});

app.use("/api/auth/login", loginLimiter);

app.use("/api/auth", authRoutes);
app.use("/api/foods", foodRoutes);
app.use("/api/orders", orderRoutes);

app.get("/", (req, res) => {
  res.send("Food Order Management API is running");
});

const PORT = process.env.PORT || 5000;

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
""",

    # =========================================================================
    # CONFIG
    # =========================================================================

    "backend/config/db.js": """
const mongoose = require("mongoose");

const connectDB = async () => {
  try {
    await mongoose.connect(process.env.MONGO_URI);

    console.log("MongoDB connected successfully");
  } catch (error) {
    console.error("MongoDB connection failed:", error.message);
    process.exit(1);
  }
};

module.exports = connectDB;
""",

    # =========================================================================
    # MODELS
    # =========================================================================

    "backend/models/User.js": """
const mongoose = require("mongoose");
const bcrypt = require("bcryptjs");

const userSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      trim: true,
    },

    email: {
      type: String,
      required: true,
      unique: true,
      lowercase: true,
    },

    password: {
      type: String,
      required: true,
    },

    role: {
      type: String,
      enum: ["customer", "admin"],
      default: "customer",
    },

    phone: {
      type: String,
    },

    address: {
      type: String,
    },
module.exports = mongoose.model("User", userSchema);
""",

    "backend/models/Food.js": """
const mongoose = require("mongoose");

const foodSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
    },

    description: {
      type: String,
      required: true,
    },

    price: {
      type: Number,
      required: true,
    },

    category: {
      type: String,
      required: true,
    },

    image: {
      type: String,
      required: true,
    },

    isAvailable: {
      type: Boolean,
      default: true,
    },
  },
  { timestamps: true }
);

module.exports = mongoose.model("Food", foodSchema);
""",

    "backend/models/Order.js": """
const mongoose = require("mongoose");

const orderSchema = new mongoose.Schema(
  {
    user: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },

    items: [
      {
        food: {
          type: mongoose.Schema.Types.ObjectId,
          ref: "Food",
        },
        name: String,
        price: Number,
        quantity: Number,
      },
    ],

    totalAmount: {
      type: Number,
      required: true,
    },

    deliveryAddress: {
      type: String,
      required: true,
    },

    phone: {
      type: String,
      required: true,
    },
module.exports = mongoose.model("Order", orderSchema);
""",

    # =========================================================================
    # CONTROLLERS
    # =========================================================================

    "backend/controllers/authController.js": """
const User = require("../models/User");
const generateToken = require("../utils/generateToken");

exports.registerUser = async (req, res) => {
  try {
    const { name, email, password, phone, address } = req.body;

    if (!name || !email || !password) {
      return res.status(400).json({
        success: false,
        message: "Name, email and password are required",
      });
    }

    const userExists = await User.findOne({ email });

    if (userExists) {
      return res.status(400).json({
        success: false,
        message: "User already exists",
      });
    }

    const user = await User.create({
      name,
      email,
      password,
      phone,
      address,
    });

    res.status(201).json({
      success: true,
      message: "User registered successfully",
      data: {
        id: user._id,
};
""",

    "backend/controllers/foodController.js": """
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
""",

    "backend/controllers/orderController.js": """
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
""",


    # =========================================================================
    # ROUTES
    # =========================================================================

    "backend/routes/authRoutes.js": """
const express = require("express");

const router = express.Router();

const {
  registerUser,
  loginUser,
  getUserProfile,
} = require("../controllers/authController");

const { protect } = require("../middleware/authMiddleware");

// Register User
router.post("/register", registerUser);

// Login User
router.post("/login", loginUser);

// Get Logged In User Profile
router.get("/profile", protect, getUserProfile);

module.exports = router;
""",

    "backend/routes/foodRoutes.js": """
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
""",

    "backend/routes/orderRoutes.js": """
const express = require("express");

const router = express.Router();

const {
  createOrder,
  getMyOrders,
  getAllOrders,
  updateOrderStatus,
} = require("../controllers/orderController");

const { protect } = require("../middleware/authMiddleware");

const adminOnly = require("../middleware/adminMiddleware");

// Customer Routes
router.post("/", protect, createOrder);

router.get("/my-orders", protect, getMyOrders);

// Admin Routes
router.get("/", protect, adminOnly, getAllOrders);

router.put(
  "/:id/status",
  protect,
  adminOnly,
  updateOrderStatus
);

module.exports = router;
""",

   

    # =========================================================================
    # MIDDLEWARE
    # =========================================================================

    "backend/middleware/authMiddleware.js": """
const jwt = require("jsonwebtoken");
const User = require("../models/User");

exports.protect = async (req, res, next) => {
  let token;

  if (
    req.headers.authorization &&
    req.headers.authorization.startsWith("Bearer")
  ) {
    try {
      token = req.headers.authorization.split(" ")[1];

      const decoded = jwt.verify(token, process.env.JWT_SECRET);

      req.user = await User.findById(decoded.id).select("-password");

      next();
    } catch (error) {
      return res.status(401).json({
        success: false,
        message: "Not authorized, token failed",
      });
    }
  }

  if (!token) {
    return res.status(401).json({
      success: false,
      message: "Not authorized, no token",
    });
  }
};

exports.adminOnly = (req, res, next) => {
  if (req.user && req.user.role === "admin") {
};
""",
    "backend/middleware/errorMiddleware.js": """
const errorHandler = (err, req, res, next) => {
  const statusCode = res.statusCode || 500;

  res.status(statusCode).json({
    success: false,
    message: err.message || "Server Error",
  });
};

module.exports = errorHandler;
""",


    # =========================================================================
    # UTILS
    # =========================================================================

    "backend/utils/generateToken.js": """
const jwt = require("jsonwebtoken");

const generateToken = (id, role) => {
  return jwt.sign({ id, role }, process.env.JWT_SECRET, {
    expiresIn: "7d",
  });
};

module.exports = generateToken;
""",

    # =========================================================================
    # FRONTEND PACKAGE
    # =========================================================================

    "frontend/package.json": """
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.16.1",
    "react": "^19.2.6",
    "react-dom": "^19.2.6",
    "react-router-dom": "^7.15.1"
  },
  "devDependencies": {
    "@eslint/js": "^10.0.1",
    "@tailwindcss/vite": "^4.3.0",
    "@types/react": "^19.2.14",
    "@types/react-dom": "^19.2.3",
    "@vitejs/plugin-react": "^6.0.1",
    "eslint": "^10.3.0",
    "eslint-plugin-react-hooks": "^7.1.1",
    "eslint-plugin-react-refresh": "^0.5.2",
    "globals": "^17.6.0",
    "tailwindcss": "^4.3.0",
    "vite": "^8.0.12"
  }
}

""",

    # =========================================================================
    # FRONTEND ENTRY
    # =========================================================================

    "frontend/src/main.jsx": """
// src/main.jsx

import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";
import "./index.css";
import { AuthProvider } from "./context/AuthContext";
import { CartProvider } from "./context/CartContext";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <CartProvider>
          <App />
        </CartProvider>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>
);
""",

    "frontend/src/App.jsx": """
// Updated src/App.jsx

import { Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";

import Home from "./pages/Home";
import Foods from "./pages/Foods";
import Cart from "./pages/Cart";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Checkout from "./pages/Checkout";
import MyOrders from "./pages/MyOrders";
import AdminDashboard from "./pages/AdminDashboard";

import ProtectedRoute from "./components/ProtectedRoute";
import AdminRoute from "./components/AdminRoute";

const App = () => {
  return (
    <>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />

        <Route path="/foods" element={<Foods />} />

        <Route path="/cart" element={<Cart />} />

        <Route path="/login" element={<Login />} />

        <Route path="/register" element={<Register />} />

        <Route
          path="/checkout"
          element={
            <ProtectedRoute>
              <Checkout />
            </ProtectedRoute>
          }
        />

        <Route
          path="/my-orders"
          element={
            <ProtectedRoute>
              <MyOrders />
            </ProtectedRoute>
          }
        />

        <Route
          path="/admin"
          element={
            <AdminRoute>
              <AdminDashboard />
            </AdminRoute>
          }
        />
      </Routes>
    </>
  );
};

export default App;
""",

    "frontend/src/index.css": """
/* src/index.css */

@import "tailwindcss";

body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}
""",

    # =========================================================================
    # API
    # =========================================================================

    "frontend/src/api/axios.js": """
// src/api/axios.js

import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:5000/api",
});

API.interceptors.request.use((req) => {
  const user = JSON.parse(localStorage.getItem("user"));

  if (user?.token) {
    req.headers.Authorization = `Bearer ${user.token}`;
  }

  return req;
});

export default API;
""",

    # =========================================================================
    # CONTEXT / REDUX
    # =========================================================================

    "frontend/src/context/AuthContext.jsx": """
// src/context/AuthContext.jsx

import { createContext, useContext, useState } from "react";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(
    JSON.parse(localStorage.getItem("user")) || null
  );

  const login = (userData) => {
    localStorage.setItem("user", JSON.stringify(userData));
    setUser(userData);
  };

  const logout = () => {
    localStorage.removeItem("user");
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
""",

    "frontend/src/context/CartContext.jsx": """
// src/context/CartContext.jsx

import { createContext, useContext, useState } from "react";

const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const [cartItems, setCartItems] = useState([]);

  const addToCart = (food) => {
    const exists = cartItems.find((item) => item._id === food._id);

    if (exists) {
      setCartItems(
        cartItems.map((item) =>
          item._id === food._id
            ? { ...item, quantity: item.quantity + 1 }
            : item
        )
      );
    } else {
      setCartItems([...cartItems, { ...food, quantity: 1 }]);
    }
  };

  const removeFromCart = (id) => {
    setCartItems(cartItems.filter((item) => item._id !== id));
  };

  const totalAmount = cartItems.reduce(
    (total, item) => total + item.price * item.quantity,
    0
  );

  return (
    <CartContext.Provider
      value={{ cartItems, addToCart, removeFromCart, totalAmount }}
    >
      {children}
    </CartContext.Provider>
  );
};

export const useCart = () => useContext(CartContext);
""",

    # =========================================================================
    # COMPONENTS
    # =========================================================================

    "frontend/src/components/Navbar.jsx": """
// src/components/Navbar.jsx

import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const Navbar = () => {
  const { user, logout } = useAuth();

  return (
    <nav className="bg-orange-500 text-white p-4 flex justify-between">
      <Link to="/" className="font-bold text-2xl">
        FoodApp
      </Link>

      <div className="flex gap-4 items-center">
        <Link to="/foods">Foods</Link>
        <Link to="/cart">Cart</Link>

        {user ? (
          <>
            <Link to="/my-orders">My Orders</Link>

            {user.role === "admin" && (
              <Link to="/admin">Admin</Link>
            )}

            <button onClick={logout}>Logout</button>
          </>
        ) : (
          <>
            <Link to="/login">Login</Link>
            <Link to="/register">Register</Link>
          </>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
""",


    "frontend/src/components/FoodCard.jsx": """
import { useCart } from "../context/CartContext";

const FoodCard = ({ food }) => {
  const { addToCart } = useCart();

  return (
    <div className="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl transition duration-300 hover:-translate-y-2">
      <img
        src={food.image}
        alt={food.name}
        className="w-full h-56 object-cover"
      />

      <div className="p-5">
        <div className="flex justify-between items-center mb-2">
          <h2 className="text-2xl font-bold text-gray-800">
            {food.name}
          </h2>

          <span className="bg-orange-100 text-orange-600 px-3 py-1 rounded-full text-sm font-semibold">
            {food.category}
          </span>
        </div>

        <p className="text-gray-600 mb-4 line-clamp-2">
          {food.description}
        </p>

        <div className="flex justify-between items-center">
          <p className="text-2xl font-bold text-orange-500">
            ₹{food.price}
          </p>

          <button
            onClick={() => addToCart(food)}
            className="bg-orange-500 hover:bg-orange-600 text-white px-5 py-2 rounded-xl font-semibold transition"
          >
            Add to Cart
          </button>
        </div>
      </div>
    </div>
  );
};

export default FoodCard;
""",

   

    "frontend/src/components/ProtectedRoute.jsx": """


import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const ProtectedRoute = ({ children }) => {
  const { user } = useAuth();

  if (!user) {
    return <Navigate to="/login" />;
  }

  return children;
};

export default ProtectedRoute;
""",

    "frontend/src/components/AdminRoute.jsx": """


import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

const AdminRoute = ({ children }) => {
  const { user } = useAuth();

  if (!user || user.role !== "admin") {
    return <Navigate to="/" />;
  }

  return children;
};

export default AdminRoute;
""",

    # =========================================================================
    # PAGES
    # =========================================================================

    "frontend/src/pages/Home.jsx": """
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <section className="bg-gradient-to-r from-orange-500 to-red-500 text-white min-h-[90vh] flex items-center justify-center px-6">
        <div className="max-w-6xl mx-auto grid md:grid-cols-2 gap-12 items-center">
          <div>
            <h1 className="text-5xl md:text-7xl font-extrabold leading-tight mb-6">
              Delicious Food
              <br />
              Delivered Fast
            </h1>

            <p className="text-xl text-orange-100 mb-8">
              Order your favorite meals anytime and enjoy hot, tasty food at your doorstep.
            </p>


             <div className="flex gap-4">
              <Link
                to="/foods"
                className="bg-white text-orange-600 px-8 py-4 rounded-2xl font-bold text-lg hover:bg-gray-100 transition"
              >
                Explore Foods
              </Link>

              <Link
                to="/register"
                className="border-2 border-white px-8 py-4 rounded-2xl font-bold text-lg hover:bg-white hover:text-orange-600 transition"
              >
                Get Started
              </Link>
            </div>

             </div>

          <div className="flex justify-center">
            <img
              src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1200&auto=format&fit=crop"
              alt="Food"
              className="rounded-3xl shadow-2xl w-full max-w-xl"
            />
          </div>
        </div>
      </section>

      <section className="py-20 px-6 bg-gray-50">
        <div className="max-w-6xl mx-auto text-center">
          <h2 className="text-4xl font-bold mb-4">
            Why Choose Us?
          </h2>

          <p className="text-gray-600 mb-14 text-lg">
            Fast delivery, fresh ingredients, and amazing taste.
          </p>


           <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-2xl shadow-lg">
              <div className="text-5xl mb-4">🍔</div>
              <h3 className="text-2xl font-bold mb-3">Fresh Food</h3>
              <p className="text-gray-600">
                Prepared with premium ingredients and hygienic cooking.
              </p>
            </div>

            <div className="bg-white p-8 rounded-2xl shadow-lg">
              <div className="text-5xl mb-4">⚡</div>
              <h3 className="text-2xl font-bold mb-3">Fast Delivery</h3>
              <p className="text-gray-600">
                Get your food delivered quickly and safely.
              </p>
            </div>


              <div className="bg-white p-8 rounded-2xl shadow-lg">
              <div className="text-5xl mb-4">⭐</div>
              <h3 className="text-2xl font-bold mb-3">Best Quality</h3>
              <p className="text-gray-600">
                Thousands of happy customers trust our service.
              </p>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Home;
""",

    "frontend/src/pages/Foods.jsx": """
import { useEffect, useState } from "react";
import FoodCard from "../components/FoodCard";

const Foods = () => {
  const [foods, setFoods] = useState([]);

  useEffect(() => {
    const dummyFoods = [
      {
        _id: 1,
        name: "Cheese Burger",
        description: "Juicy beef burger with melted cheese and crispy fries.",
        price: 249,
        category: "Burger",
        image:
          "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?q=80&w=1200&auto=format&fit=crop",
      },
      {
        _id: 2,
        name: "Pepperoni Pizza",
        description: "Classic pepperoni pizza with extra mozzarella cheese.",
        price: 499,
        category: "Pizza",
         image:
          "https://images.unsplash.com/photo-1513104890138-7c749659a591?q=80&w=1200&auto=format&fit=crop",
      },
      {
        _id: 3,
        name: "Pasta Alfredo",
        description: "Creamy Alfredo pasta served with garlic bread.",
        price: 349,
        category: "Pasta",
        image:
          "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?q=80&w=1200&auto=format&fit=crop",
      },
      {
        _id: 4,
        name: "Chicken Biryani",
        description: "Aromatic chicken biryani with spicy masala flavors.",
        price: 399,
        category: "Biryani",
        image:
          "https://images.unsplash.com/photo-1631515243349-e0cb75fb8d3a?q=80&w=1200&auto=format&fit=crop",
      },

       {
        _id: 5,
        name: "Chocolate Shake",
        description: "Rich chocolate milkshake topped with whipped cream.",
        price: 199,
        category: "Drinks",
        image:
          "https://images.unsplash.com/photo-1577805947697-89e18249d767?q=80&w=1200&auto=format&fit=crop",
      },
      {
        _id: 6,
        name: "Veg Momos",
        description: "Steamed veg momos served with spicy chutney.",
        price: 149,
        category: "Snacks",
        image:
          "https://images.unsplash.com/photo-1626776876729-bab4369a5a5f?q=80&w=1200&auto=format&fit=crop",
      },
    ];

    setFoods(dummyFoods);
  }, []);

  return (
    <div className="min-h-screen bg-gray-100 py-12 px-6">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-extrabold text-gray-800 mb-4">
            Our Delicious Menu
          </h1>

          <p className="text-lg text-gray-600 max-w-2xl mx-auto">
            Explore our wide range of delicious meals prepared with fresh ingredients.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {foods.map((food) => (
            <FoodCard key={food._id} food={food} />
          ))}
        </div>
      </div>
    </div>
  );
};
export default Foods;
""",

   

    "frontend/src/pages/Cart.jsx": """
// src/pages/AdminDashboard.jsx

const AdminDashboard = () => {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold">Admin Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Orders</h2>
          <p className="text-2xl font-bold">120</p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Foods</h2>
          <p className="text-2xl font-bold">45</p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Users</h2>
          <p className="text-2xl font-bold">300</p>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
""",

    "frontend/src/pages/Checkout.jsx": """
// src/pages/Register.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";
import { useAuth } from "../context/AuthContext";

const Register = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    phone: "",
    address: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await API.post("/auth/register", formData);

      login(res.data.data);

      navigate("/");
    } catch (error) {
      alert(error.response?.data?.message || "Registration failed");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-[80vh]">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 shadow-lg rounded-xl w-96"
      >
        <h1 className="text-3xl font-bold mb-6 text-center">
          Register
        </h1>

        <input
          type="text"
          name="name"
          placeholder="Name"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="text"
          name="phone"
          placeholder="Phone"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <textarea
          name="address"
          placeholder="Address"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <button className="w-full bg-orange-500 text-white py-3 rounded">
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;
""",

    "frontend/src/pages/Login.jsx": """
// src/pages/Login.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";
import { useAuth } from "../context/AuthContext";

const Login = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await API.post("/auth/login", formData);

      login(res.data.data);

      navigate("/");
    } catch (error) {
      alert(error.response?.data?.message || "Login failed");
    }
  };

  return (
    <div className="flex justify-center items-center h-[80vh]">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 shadow-lg rounded-xl w-96"
      >
        <h1 className="text-3xl font-bold mb-6 text-center">
          Login
        </h1>

        <input
          type="email"
          name="email"
          placeholder="Email"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <button className="w-full bg-orange-500 text-white py-3 rounded">
          Login
        </button>
      </form>
    </div>
  );
};

export default Login;
""",

    "frontend/src/pages/Register.jsx": """
// src/pages/Register.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../api/axios";
import { useAuth } from "../context/AuthContext";

const Register = () => {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    phone: "",
    address: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await API.post("/auth/register", formData);

      login(res.data.data);

      navigate("/");
    } catch (error) {
      alert(error.response?.data?.message || "Registration failed");
    }
  };

  return (
    <div className="flex justify-center items-center min-h-[80vh]">
      <form
        onSubmit={handleSubmit}
        className="bg-white p-8 shadow-lg rounded-xl w-96"
      >
        <h1 className="text-3xl font-bold mb-6 text-center">
          Register
        </h1>

        <input
          type="text"
          name="name"
          placeholder="Name"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <input
          type="text"
          name="phone"
          placeholder="Phone"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <textarea
          name="address"
          placeholder="Address"
          className="w-full border p-3 rounded mb-4"
          onChange={handleChange}
        />

        <button className="w-full bg-orange-500 text-white py-3 rounded">
          Register
        </button>
      </form>
    </div>
  );
};

export default Register;
""",

    "frontend/src/pages/MyOrders.jsx": """
// src/pages/MyOrders.jsx

import { useEffect, useState } from "react";
import API from "../api/axios";

const MyOrders = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const res = await API.get("/orders/my-orders");

        setOrders(res.data.data);
      } catch (error) {
        console.log(error);
      }
    };

    fetchOrders();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">
        My Orders
      </h1>

      {orders.length === 0 ? (
        <p>No orders found.</p>
      ) : (
        <div className="space-y-6">
          {orders.map((order) => (
            <div
              key={order._id}
              className="bg-white shadow-md rounded-xl p-6"
            >
              <h2 className="text-xl font-bold mb-2">
                Order ID: {order._id}
              </h2>

              <p className="mb-2">
                Status:
                <span className="font-semibold ml-2">
                  {order.orderStatus}
                </span>
              </p>

              <p className="mb-2">
                Total: ₹{order.totalAmount}
              </p>

              <div className="mt-4">
                {order.items.map((item, index) => (
                  <div key={index} className="border-b py-2">
                    <p>
                      {item.name} x {item.quantity}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default MyOrders;
""",

    "frontend/src/pages/AdminDashboard.jsx": """
// src/pages/AdminDashboard.jsx

const AdminDashboard = () => {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold">Admin Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Orders</h2>
          <p className="text-2xl font-bold">120</p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Foods</h2>
          <p className="text-2xl font-bold">45</p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Users</h2>
          <p className="text-2xl font-bold">300</p>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;
""",

  

    # =========================================================================
    # PUBLIC
    # =========================================================================

    "frontend/public/index.html": """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>frontend</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.jsx"></script>
  </body>
</html>

""",

    # =========================================================================
    # README
    # =========================================================================

    "README.md": """
# MERN Food Order Management System

## Setup Instructions

### Backend
cd backend
npm install
npm run dev

### Frontend
cd frontend
npm install
npm run dev
"""
}

# =============================================================================
# GENERATE WORKSPACE
# =============================================================================

def generate_workspace():
    root_dir = os.getcwd()

    print("=" * 70)
    print("Generating MERN Food Order Management Workspace")
    print("=" * 70)

    for relative_path, content in WORKSPACE_FILES.items():

        file_path = os.path.join(root_dir, relative_path)

        folder_path = os.path.dirname(file_path)

        os.makedirs(folder_path, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content.strip())

        print(f"Created: {relative_path}")

    print("\nProject generated successfully.")
    print("=" * 70)


# =============================================================================
# MAIN
# =============================================================================

if __name__ == "__main__":
    generate_workspace()
