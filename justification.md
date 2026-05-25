# **Response A**

# **Food Order Management Website — MERN Stack Response**

Excellent. Based on the requirements, we will build a **production-ready Food Order Management System** using the **MERN Stack**.

We will use:

* **MongoDB** for database  
* **Express.js** for backend APIs  
* **React.js** for frontend  
* **Node.js** as backend runtime  
* **JWT** for authentication  
* **bcrypt** for password hashing  
* **Tailwind CSS** for UI  
* **Axios** for API communication  
* **React Router** for routing  
* **Context API / Redux Toolkit** for cart and auth state

---

# **System Architecture**

food-order-management/  
│  
├── backend/  
│   ├── config/  
│   │   └── db.js  
│   │  
│   ├── controllers/  
│   │   ├── authController.js  
│   │   ├── foodController.js  
│   │   ├── orderController.js  
│   │   └── adminController.js  
│   │  
│   ├── middleware/  
│   │   ├── authMiddleware.js  
│   │   ├── adminMiddleware.js  
│   │   └── errorMiddleware.js  
│   │  
│   ├── models/  
│   │   ├── User.js  
│   │   ├── Food.js  
│   │   └── Order.js  
│   │  
│   ├── routes/  
│   │   ├── authRoutes.js  
│   │   ├── foodRoutes.js  
│   │   ├── orderRoutes.js  
│   │   └── adminRoutes.js  
│   │  
│   ├── server.js  
│   └── .env  
│  
└── frontend/  
   ├── src/  
   │   ├── components/  
   │   │   ├── Navbar.jsx  
   │   │   ├── FoodCard.jsx  
   │   │   ├── ProtectedRoute.jsx  
   │   │   └── AdminRoute.jsx  
   │   │  
   │   ├── pages/  
   │   │   ├── Home.jsx  
   │   │   ├── Foods.jsx  
   │   │   ├── Cart.jsx  
   │   │   ├── Checkout.jsx  
   │   │   ├── Login.jsx  
   │   │   ├── Register.jsx  
   │   │   ├── MyOrders.jsx  
   │   │   └── AdminDashboard.jsx  
   │   │  
   │   ├── context/  
   │   │   ├── AuthContext.jsx  
   │   │   └── CartContext.jsx  
   │   │  
   │   ├── api/  
   │   │   └── axios.js  
   │   │  
   │   ├── App.jsx  
   │   └── main.jsx  
---

# **Backend Implementation**

## **1\. Server Setup**

// backend/server.js

const express \= require("express");  
const dotenv \= require("dotenv");  
const cors \= require("cors");  
const rateLimit \= require("express-rate-limit");  
const connectDB \= require("./config/db");

const authRoutes \= require("./routes/authRoutes");  
const foodRoutes \= require("./routes/foodRoutes");  
const orderRoutes \= require("./routes/orderRoutes");  
const adminRoutes \= require("./routes/adminRoutes");

dotenv.config();  
connectDB();

const app \= express();

app.use(express.json());  
app.use(cors());

const loginLimiter \= rateLimit({  
 windowMs: 15 \* 60 \* 1000,  
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
app.use("/api/admin", adminRoutes);

app.get("/", (req, res) \=\> {  
 res.send("Food Order Management API is running");  
});

const PORT \= process.env.PORT || 5000;

app.listen(PORT, () \=\> {  
 console.log(\`Server running on port ${PORT}\`);  
});  
---

## **2\. MongoDB Connection**

// backend/config/db.js

const mongoose \= require("mongoose");

const connectDB \= async () \=\> {  
 try {  
   await mongoose.connect(process.env.MONGO\_URI);  
   console.log("MongoDB connected successfully");  
 } catch (error) {  
   console.error("MongoDB connection failed:", error.message);  
   process.exit(1);  
 }  
};

module.exports \= connectDB;  
---

# **Database Models**

## **User Model**

// backend/models/User.js

const mongoose \= require("mongoose");  
const bcrypt \= require("bcryptjs");

const userSchema \= new mongoose.Schema(  
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
     enum: \["customer", "admin"\],  
     default: "customer",  
   },

   phone: {  
     type: String,  
   },

   address: {  
     type: String,  
   },  
 },  
 { timestamps: true }  
);

userSchema.pre("save", async function (next) {  
 if (\!this.isModified("password")) return next();

 const salt \= await bcrypt.genSalt(10);  
 this.password \= await bcrypt.hash(this.password, salt);

 next();  
});

userSchema.methods.matchPassword \= async function (enteredPassword) {  
 return await bcrypt.compare(enteredPassword, this.password);  
};

module.exports \= mongoose.model("User", userSchema);  
---

## **Food Model**

// backend/models/Food.js

const mongoose \= require("mongoose");

const foodSchema \= new mongoose.Schema(  
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

module.exports \= mongoose.model("Food", foodSchema);  
---

## **Order Model**

// backend/models/Order.js

const mongoose \= require("mongoose");

const orderSchema \= new mongoose.Schema(  
 {  
   user: {  
     type: mongoose.Schema.Types.ObjectId,  
     ref: "User",  
     required: true,  
   },

   items: \[  
     {  
       food: {  
         type: mongoose.Schema.Types.ObjectId,  
         ref: "Food",  
       },  
       name: String,  
       price: Number,  
       quantity: Number,  
     },  
   \],

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

   paymentMethod: {  
     type: String,  
     enum: \["COD", "Online"\],  
     default: "COD",  
   },

   orderStatus: {  
     type: String,  
     enum: \[  
       "Pending",  
       "Confirmed",  
       "Preparing",  
       "Out for Delivery",  
       "Delivered",  
       "Cancelled",  
     \],  
     default: "Pending",  
   },  
 },  
 { timestamps: true }  
);

module.exports \= mongoose.model("Order", orderSchema);  
---

# **Authentication Flow**

## **JWT Token Generator**

// backend/utils/generateToken.js

const jwt \= require("jsonwebtoken");

const generateToken \= (id, role) \=\> {  
 return jwt.sign({ id, role }, process.env.JWT\_SECRET, {  
   expiresIn: "7d",  
 });  
};

module.exports \= generateToken;  
---

## **Auth Controller**

// backend/controllers/authController.js

const User \= require("../models/User");  
const generateToken \= require("../utils/generateToken");

exports.registerUser \= async (req, res) \=\> {  
 try {  
   const { name, email, password, phone, address } \= req.body;

   if (\!name || \!email || \!password) {  
     return res.status(400).json({  
       success: false,  
       message: "Name, email and password are required",  
     });  
   }

   const userExists \= await User.findOne({ email });

   if (userExists) {  
     return res.status(400).json({  
       success: false,  
       message: "User already exists",  
     });  
   }

   const user \= await User.create({  
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
       id: user.\_id,  
       name: user.name,  
       email: user.email,  
       role: user.role,  
       token: generateToken(user.\_id, user.role),  
     },  
   });  
 } catch (error) {  
   res.status(500).json({  
     success: false,  
     message: "Server error during registration",  
   });  
 }  
};

exports.loginUser \= async (req, res) \=\> {  
 try {  
   const { email, password } \= req.body;

   const user \= await User.findOne({ email });

   if (user && (await user.matchPassword(password))) {  
     res.json({  
       success: true,  
       message: "Login successful",  
       data: {  
         id: user.\_id,  
         name: user.name,  
         email: user.email,  
         role: user.role,  
         token: generateToken(user.\_id, user.role),  
       },  
     });  
   } else {  
     res.status(401).json({  
       success: false,  
       message: "Invalid email or password",  
     });  
   }  
 } catch (error) {  
   res.status(500).json({  
     success: false,  
     message: "Server error during login",  
   });  
 }  
};  
---

# **Middleware**

## **Auth Middleware**

// backend/middleware/authMiddleware.js

const jwt \= require("jsonwebtoken");  
const User \= require("../models/User");

exports.protect \= async (req, res, next) \=\> {  
 let token;

 if (  
   req.headers.authorization &&  
   req.headers.authorization.startsWith("Bearer")  
 ) {  
   try {  
     token \= req.headers.authorization.split(" ")\[1\];

     const decoded \= jwt.verify(token, process.env.JWT\_SECRET);

     req.user \= await User.findById(decoded.id).select("-password");

     next();  
   } catch (error) {  
     return res.status(401).json({  
       success: false,  
       message: "Not authorized, token failed",  
     });  
   }  
 }

 if (\!token) {  
   return res.status(401).json({  
     success: false,  
     message: "Not authorized, no token",  
   });  
 }  
};

exports.adminOnly \= (req, res, next) \=\> {  
 if (req.user && req.user.role \=== "admin") {  
   next();  
 } else {  
   res.status(403).json({  
     success: false,  
     message: "Admin access only",  
   });  
 }  
};  
---

# **Food Controller**

// backend/controllers/foodController.js

const Food \= require("../models/Food");

exports.getFoods \= async (req, res) \=\> {  
 try {  
   const foods \= await Food.find({ isAvailable: true });

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

exports.createFood \= async (req, res) \=\> {  
 try {  
   const { name, description, price, category, image } \= req.body;

   const food \= await Food.create({  
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

exports.updateFood \= async (req, res) \=\> {  
 try {  
   const food \= await Food.findByIdAndUpdate(req.params.id, req.body, {  
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
 }  
};

exports.deleteFood \= async (req, res) \=\> {  
 try {  
   await Food.findByIdAndDelete(req.params.id);

   res.json({  
     success: true,  
     message: "Food item deleted successfully",  
   });  
 } catch (error) {  
   res.status(500).json({  
     success: false,  
     message: "Failed to delete food item",  
   });  
 }  
};  
---

# **Order Controller**

// backend/controllers/orderController.js

const Order \= require("../models/Order");

exports.createOrder \= async (req, res) \=\> {  
 try {  
   const { items, totalAmount, deliveryAddress, phone, paymentMethod } \=  
     req.body;

   if (\!items || items.length \=== 0\) {  
     return res.status(400).json({  
       success: false,  
       message: "Cart is empty",  
     });  
   }

   const order \= await Order.create({  
     user: req.user.\_id,  
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

exports.getMyOrders \= async (req, res) \=\> {  
 try {  
   const orders \= await Order.find({ user: req.user.\_id }).sort({  
     createdAt: \-1,  
   });

   res.json({  
     success: true,  
     data: orders,  
   });  
 } catch (error) {  
   res.status(500).json({  
     success: false,  
     message: "Failed to fetch orders",  
   });  
 }  
};

exports.getAllOrders \= async (req, res) \=\> {  
 try {  
   const orders \= await Order.find()  
     .populate("user", "name email")  
     .sort({ createdAt: \-1 });

   res.json({  
     success: true,  
     data: orders,  
   });  
 } catch (error) {  
   res.status(500).json({  
     success: false,  
     message: "Failed to fetch all orders",  
   });  
 }  
};

exports.updateOrderStatus \= async (req, res) \=\> {  
 try {  
   const { orderStatus } \= req.body;

   const order \= await Order.findByIdAndUpdate(  
     req.params.id,  
     { orderStatus },  
     { new: true }  
   );

   res.json({  
     success: true,  
     message: "Order status updated successfully",  
     data: order,  
   });  
 } catch (error) {  
   res.status(500).json({  
     success: false,  
     message: "Failed to update order status",  
   });  
 }  
};  
---

# **Routes**

## **Auth Routes**

// backend/routes/authRoutes.js

const express \= require("express");  
const { registerUser, loginUser } \= require("../controllers/authController");

const router \= express.Router();

router.post("/register", registerUser);  
router.post("/login", loginUser);

module.exports \= router;

## **Food Routes**

// backend/routes/foodRoutes.js

const express \= require("express");  
const {  
 getFoods,  
 createFood,  
 updateFood,  
 deleteFood,  
} \= require("../controllers/foodController");

const { protect, adminOnly } \= require("../middleware/authMiddleware");

const router \= express.Router();

router.get("/", getFoods);  
router.post("/", protect, adminOnly, createFood);  
router.put("/:id", protect, adminOnly, updateFood);  
router.delete("/:id", protect, adminOnly, deleteFood);

module.exports \= router;

## **Order Routes**

// backend/routes/orderRoutes.js

const express \= require("express");  
const {  
 createOrder,  
 getMyOrders,  
 getAllOrders,  
 updateOrderStatus,  
} \= require("../controllers/orderController");

const { protect, adminOnly } \= require("../middleware/authMiddleware");

const router \= express.Router();

router.post("/", protect, createOrder);  
router.get("/my-orders", protect, getMyOrders);  
router.get("/", protect, adminOnly, getAllOrders);  
router.put("/:id/status", protect, adminOnly, updateOrderStatus);

module.exports \= router;  
---

# **Frontend Implementation**

## **Axios Setup**

// frontend/src/api/axios.js

import axios from "axios";

const API \= axios.create({  
 baseURL: "http://localhost:5000/api",  
});

API.interceptors.request.use((req) \=\> {  
 const user \= JSON.parse(localStorage.getItem("user"));

 if (user?.token) {  
   req.headers.Authorization \= \`Bearer ${user.token}\`;  
 }

 return req;  
});

export default API;  
---

## **Cart Context**

// frontend/src/context/CartContext.jsx

import { createContext, useContext, useState } from "react";

const CartContext \= createContext();

export const CartProvider \= ({ children }) \=\> {  
 const \[cartItems, setCartItems\] \= useState(\[\]);

 const addToCart \= (food) \=\> {  
   const exists \= cartItems.find((item) \=\> item.\_id \=== food.\_id);

   if (exists) {  
     setCartItems(  
       cartItems.map((item) \=\>  
         item.\_id \=== food.\_id  
           ? { ...item, quantity: item.quantity \+ 1 }  
           : item  
       )  
     );  
   } else {  
     setCartItems(\[...cartItems, { ...food, quantity: 1 }\]);  
   }  
 };

 const removeFromCart \= (id) \=\> {  
   setCartItems(cartItems.filter((item) \=\> item.\_id \!== id));  
 };

 const totalAmount \= cartItems.reduce(  
   (total, item) \=\> total \+ item.price \* item.quantity,  
   0  
 );

 return (  
   \<CartContext.Provider  
     value={{ cartItems, addToCart, removeFromCart, totalAmount }}  
   \>  
     {children}  
   \</CartContext.Provider\>  
 );  
};

export const useCart \= () \=\> useContext(CartContext);  
---

## **Food Card Component**

// frontend/src/components/FoodCard.jsx

import { useCart } from "../context/CartContext";

const FoodCard \= ({ food }) \=\> {  
 const { addToCart } \= useCart();

 return (  
   \<div className="bg-white shadow-md rounded-xl overflow-hidden"\>  
     \<img  
       src={food.image}  
       alt={food.name}  
       className="w-full h-48 object-cover"  
     /\>

     \<div className="p-4"\>  
       \<h3 className="text-xl font-semibold"\>{food.name}\</h3\>  
       \<p className="text-gray-600"\>{food.description}\</p\>  
       \<p className="font-bold mt-2"\>₹{food.price}\</p\>

       \<button  
         onClick={() \=\> addToCart(food)}  
         className="mt-4 w-full bg-orange-500 text-white py-2 rounded-lg"  
       \>  
         Add to Cart  
       \</button\>  
     \</div\>  
   \</div\>  
 );  
};

export default FoodCard;  
---

## **Foods Page**

// frontend/src/pages/Foods.jsx

import { useEffect, useState } from "react";  
import API from "../api/axios";  
import FoodCard from "../components/FoodCard";

const Foods \= () \=\> {  
 const \[foods, setFoods\] \= useState(\[\]);

 useEffect(() \=\> {  
   const fetchFoods \= async () \=\> {  
     const res \= await API.get("/foods");  
     setFoods(res.data.data);  
   };

   fetchFoods();  
 }, \[\]);

 return (  
   \<div className="p-6 grid grid-cols-1 md:grid-cols-3 gap-6"\>  
     {foods.map((food) \=\> (  
       \<FoodCard key={food.\_id} food={food} /\>  
     ))}  
   \</div\>  
 );  
};

export default Foods;  
---

## **Cart Page**

// frontend/src/pages/Cart.jsx

import { useCart } from "../context/CartContext";  
import { Link } from "react-router-dom";

const Cart \= () \=\> {  
 const { cartItems, removeFromCart, totalAmount } \= useCart();

 return (  
   \<div className="p-6"\>  
     \<h1 className="text-2xl font-bold"\>Your Cart\</h1\>

     {cartItems.length \=== 0 ? (  
       \<p\>Your cart is empty.\</p\>  
     ) : (  
       \<\>  
         {cartItems.map((item) \=\> (  
           \<div  
             key={item.\_id}  
             className="flex justify-between items-center border-b py-4"  
           \>  
             \<div\>  
               \<h3\>{item.name}\</h3\>  
               \<p\>  
                 ₹{item.price} x {item.quantity}  
               \</p\>  
             \</div\>

             \<button  
               onClick={() \=\> removeFromCart(item.\_id)}  
               className="text-red-500"  
             \>  
               Remove  
             \</button\>  
           \</div\>  
         ))}

         \<h2 className="text-xl font-bold mt-4"\>  
           Total: ₹{totalAmount}  
         \</h2\>

         \<Link  
           to="/checkout"  
           className="inline-block mt-4 bg-green-600 text-white px-4 py-2 rounded"  
         \>  
           Proceed to Checkout  
         \</Link\>  
       \</\>  
     )}  
   \</div\>  
 );  
};

export default Cart;  
---

# **Admin Dashboard**

The admin dashboard will allow restaurant staff to:

* View total orders  
* View total users  
* View total food items  
* Add food items  
* Edit food items  
* Delete food items  
* Update order status

// frontend/src/pages/AdminDashboard.jsx

const AdminDashboard \= () \=\> {  
 return (  
   \<div className="p-6"\>  
     \<h1 className="text-3xl font-bold"\>Admin Dashboard\</h1\>

     \<div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6"\>  
       \<div className="bg-white shadow p-6 rounded-xl"\>  
         \<h2\>Total Orders\</h2\>  
         \<p className="text-2xl font-bold"\>120\</p\>  
       \</div\>

       \<div className="bg-white shadow p-6 rounded-xl"\>  
         \<h2\>Total Foods\</h2\>  
         \<p className="text-2xl font-bold"\>45\</p\>  
       \</div\>

       \<div className="bg-white shadow p-6 rounded-xl"\>  
         \<h2\>Total Users\</h2\>  
         \<p className="text-2xl font-bold"\>300\</p\>  
       \</div\>  
     \</div\>  
   \</div\>  
 );  
};

export default AdminDashboard;  
---

# **Application Flow**

1\. User registers or logs in.  
2\. JWT token is stored in localStorage.  
3\. User browses food items.  
4\. User adds food items to cart.  
5\. Cart calculates total amount.  
6\. The user places an order from the checkout page.  
7\. Backend verifies JWT token.  
8\. Order is stored in MongoDB.  
9\. Admin views order in dashboard.  
10\. Admin updates order status.  
11\. User can track order status from My Orders page.  
---

# **Environment Variables**

PORT=5000  
MONGO\_URI=mongodb+srv://username:password@cluster.mongodb.net/food-order-db  
JWT\_SECRET=your\_jwt\_secret\_key  
NODE\_ENV=development  
---

# **Setup Commands**

## **Backend**

cd backend  
npm init \-y  
npm install express mongoose dotenv cors bcryptjs jsonwebtoken express-rate-limit  
npm install nodemon \--save-dev  
npm run dev

## **Frontend**

cd frontend  
npm create vite@latest  
npm install  
npm install axios react-router-dom  
npm install \-D tailwindcss postcss autoprefixer  
npm run dev  
---

# **Deployment Plan**

Frontend can be deployed on:

* Vercel  
* Netlify

Backend can be deployed on:

* Render  
* Railway  
* Cyclic

Database can be hosted on:

* MongoDB Atlas

---

# 

# **Final Output**

The final application will have:

* Working customer login/register flow  
* Food browsing system  
* Cart management  
* Checkout system  
* Order placement  
* User order history  
* Admin dashboard  
* Food item CRUD  
* Order status update  
* MongoDB database storage  
* JWT authentication  
* Responsive UI  
* Secure backend APIs

---

# **Conclusion**

This MERN Food Order Management System provides a complete end-to-end working flow from customer food browsing to order placement and admin order management.

It is modular, scalable, secure, and ready for future features like payment gateway, email notifications, food image upload, and delivery partner tracking.

**Ratings & Evaluations (RLHF)**

Dimension 1: Correctness — 4/5

The response is mostly correct and follows the MERN stack properly. Backend models, routes, controllers, JWT auth, bcrypt password hashing, cart logic, and order flow are logically valid. Minor issues exist: \`utils/generateToken.js\` was used but not shown in the main folder structure, admin routes/controller are mentioned but not fully implemented, and frontend auth context/protected routes are not fully coded.

Dimension 2: Relevance — 4/5

The response is highly relevant to the given prompt. It covers food listing, cart, checkout, authentication, admin dashboard, food CRUD, order status management, MongoDB storage, and deployment guidance, which directly match the prompt requirements. However, optional features like payment gateway, Cloudinary image upload, and email notification are only mentioned, not implemented.

Dimension 3: Completeness — 4/5

The response gives a strong architecture and useful backend/frontend code snippets, but it is not a fully complete project. Missing pieces include complete login/register frontend, checkout page implementation, user order history page, admin food management UI, admin order management UI, profile API, admin dashboard API, and full deployment steps. So it is a good blueprint, but not a complete runnable app yet.

Dimension 4: Style & Presentation — 4/5

The response is well-structured, clean, and easy to understand. It uses proper headings, folder structure, code blocks, and separates backend, frontend, database, routes, and flow clearly. The presentation is professional and close to the format of the original sample response.

Dimension 5: Coherence — 4/5

The explanation flows logically from system architecture → backend → models → controllers → routes → frontend → deployment. The customer and admin flow is easy to follow. Minor coherence issue: some files are referenced but not fully created, such as \`adminController.js\`, \`adminRoutes.js\`, \`ProtectedRoute.jsx\`, and \`AuthContext.jsx\`.

Dimension 6: Helpfulness — 4/5

The response is useful for a student or developer to understand how a MERN food ordering website should be built. It provides enough code to start development and explains the complete system flow. But for real implementation, the developer would still need to fill missing frontend pages, admin APIs, validation, image upload, and deployment configuration.

Dimension 7: Creativity — 4/5

The response follows a standard MERN architecture and includes practical features like admin dashboard, order status, JWT auth, and cart context. However, it does not introduce advanced creative features like live order tracking, restaurant analytics, recommendation system, real-time updates using Socket.io, or modern UI animations.

# **Response B**

# **Food Order Management Website — MERN Stack (Production-Ready)**

## **1\. Project Architecture & Directory Structure**

A clean, modular separation of concerns ensures maintainability and seamless horizontal scaling.

food-order-management/

├── backend/  
│   ├── config/  
│   │   └── db.js  
│   ├── controllers/  
│   │   ├── authController.js  
│   │   ├── foodController.js  
│   │   ├── orderController.js  
│   │   └── adminController.js  
│   ├── middleware/  
│   │   ├── authMiddleware.js  
│   │   └── errorMiddleware.js  
│   ├── models/  
│   │   ├── User.js  
│   │   ├── Food.js  
│   │   └── Order.js  
│   ├── routes/  
│   │   ├── authRoutes.js  
│   │   ├── foodRoutes.js  
│   │   ├── orderRoutes.js  
│   │   └── adminRoutes.js  
│   ├── .env  
│   ├── package.json  
│   └── server.js

└── frontend/  
    ├── public/  
    ├── src/  
    │   ├── assets/  
    │   ├── components/  
    │   │   ├── Navbar.jsx  
    │   │   ├── ProtectedRoute.jsx  
    │   │   └── FoodCard.jsx  
    │   ├── context/  
    │   │   └── AuthContext.jsx  
    │   ├── redux/  
    │   │   ├── store.js  
    │   │   └── cartSlice.js  
    │   ├── pages/  
    │   │   ├── Home.jsx  
    │   │   ├── Cart.jsx  
    │   │   ├── Checkout.jsx  
    │   │   ├── Login.jsx  
    │   │   ├── Register.jsx  
    │   │   ├── OrderHistory.jsx  
    │   │   └── Admin/  
    │   │       ├── Dashboard.jsx  
    │   │       ├── FoodManagement.jsx  
    │   │       └── OrderManagement.jsx  
    │   ├── App.jsx  
    │   ├── index.css  
    │   └── main.jsx  
    ├── package.json  
    └── tailwind.config.js

---

# **2\. Backend Implementation (Node.js \+ Express \+ MongoDB)**

## **backend/package.json**

{  
  "name": "food-order-backend",  
  "version": "1.0.0",  
  "main": "server.js",  
  "type": "module",  
  "scripts": {  
    "start": "node server.js",  
    "dev": "nodemon server.js"  
  },  
  "dependencies": {  
    "bcryptjs": "^2.4.3",  
    "cors": "^2.8.5",  
    "dotenv": "^16.4.5",  
    "express": "^4.19.2",  
    "express-rate-limit": "^7.2.0",  
    "jsonwebtoken": "^9.0.2",  
    "mongoose": "^8.3.1"  
  }  
}

---

## **backend/.env**

PORT=5000

MONGO\_URI=mongodb+srv://\<username\>:\<password\>@cluster0.mongodb.net/foodOrderDB?retryWrites=true\&w=majority

JWT\_SECRET=super\_secret\_session\_key\_high\_entropy\_123\!

NODE\_ENV=production

---

## **backend/config/db.js**

import mongoose from 'mongoose';

const connectDB \= async () \=\> {  
  try {  
    const conn \= await mongoose.connect(process.env.MONGO\_URI);

    console.log(\`MongoDB Connected: ${conn.connection.host}\`);  
  } catch (error) {  
    console.error(\`Database Connection Error: ${error.message}\`);  
    process.exit(1);  
  }  
};

export default connectDB;

---

# **Mongoose Models**

## **backend/models/User.js**

import mongoose from 'mongoose';  
import bcrypt from 'bcryptjs';

const userSchema \= new mongoose.Schema({  
  name: { type: String, required: true, trim: true },

  email: {  
    type: String,  
    required: true,  
    unique: true,  
    lowercase: true,  
    trim: true  
  },

  password: { type: String, required: true },

  role: {  
    type: String,  
    enum: \['customer', 'admin'\],  
    default: 'customer'  
  },

  phone: { type: String, required: true },

  address: { type: String, required: true }

}, { timestamps: true });

userSchema.pre('save', async function (next) {

  if (\!this.isModified('password')) return next();

  const salt \= await bcrypt.genSalt(10);

  this.password \= await bcrypt.hash(this.password, salt);

  next();

});

userSchema.methods.matchPassword \= async function (enteredPassword) {  
  return await bcrypt.compare(enteredPassword, this.password);  
};

export default mongoose.model('User', userSchema);

---

## **backend/models/Food.js**

import mongoose from 'mongoose';

const foodSchema \= new mongoose.Schema({

  name: { type: String, required: true, trim: true },

  description: { type: String, required: true },

  price: { type: Number, required: true, min: 0 },

  category: { type: String, required: true, index: true },

  image: { type: String, required: true },

  isAvailable: { type: Boolean, default: true }

}, { timestamps: true });

export default mongoose.model('Food', foodSchema);

---

## **backend/models/Order.js**

import mongoose from 'mongoose';

const orderSchema \= new mongoose.Schema({

  user: {  
    type: mongoose.Schema.Types.ObjectId,  
    ref: 'User',  
    required: true  
  },

  items: \[  
    {  
      food: {  
        type: mongoose.Schema.Types.ObjectId,  
        ref: 'Food',  
        required: true  
      },

      quantity: {  
        type: Number,  
        required: true,  
        min: 1  
      },

      price: {  
        type: Number,  
        required: true  
      }  
    }  
  \],

  totalAmount: { type: Number, required: true },

  deliveryAddress: { type: String, required: true },

  phone: { type: String, required: true },

  paymentMethod: {  
    type: String,  
    enum: \['COD', 'Card'\],  
    default: 'COD'  
  },

  orderStatus: {  
    type: String,  
    enum: \[  
      'Pending',  
      'Confirmed',  
      'Preparing',  
      'Out for Delivery',  
      'Delivered',  
      'Cancelled'  
    \],  
    default: 'Pending'  
  }

}, { timestamps: true });

export default mongoose.model('Order', orderSchema);

---

# **Middleware**

## **backend/middleware/authMiddleware.js**

import jwt from 'jsonwebtoken';  
import User from '../models/User.js';

export const protect \= async (req, res, next) \=\> {

  let token \= req.headers.authorization?.startsWith('Bearer')  
    ? req.headers.authorization.split(' ')\[1\]  
    : null;

  if (\!token) {  
    return res.status(401).json({  
      success: false,  
      message: 'Not authorized, token missing'  
    });  
  }

  try {

    const decoded \= jwt.verify(token, process.env.JWT\_SECRET);

    req.user \= await User.findById(decoded.id).select('-password');

    if (\!req.user) {  
      return res.status(404).json({  
        success: false,  
        message: 'User not found'  
      });  
    }

    next();

  } catch (error) {

    return res.status(401).json({  
      success: false,  
      message: 'Not authorized, token invalid'  
    });

  }

};

export const adminOnly \= (req, res, next) \=\> {

  if (req.user && req.user.role \=== 'admin') {  
    next();  
  } else {  
    res.status(403).json({  
      success: false,  
      message: 'Access denied: Admin resource'  
    });  
  }

};

---

## **backend/middleware/errorMiddleware.js**

export const errorHandler \= (err, req, res, next) \=\> {

  const statusCode \= res.statusCode \=== 200 ? 500 : res.statusCode;

  res.status(statusCode).json({  
    success: false,  
    message: err.message,  
    stack: process.env.NODE\_ENV \=== 'production'  
      ? null  
      : err.stack,  
  });

};

---

# **Controllers**

## **backend/controllers/authController.js**

import User from '../models/User.js';  
import jwt from 'jsonwebtoken';

const generateToken \= (id) \=\>  
  jwt.sign({ id }, process.env.JWT\_SECRET, {  
    expiresIn: '7d'  
  });

export const registerUser \= async (req, res, next) \=\> {

  try {

    const { name, email, password, phone, address } \= req.body;

    if (await User.findOne({ email })) {

      res.status(400);  
      throw new Error('User already exists with this email');

    }

    const user \= await User.create({  
      name,  
      email,  
      password,  
      phone,  
      address  
    });

    res.status(201).json({  
      success: true,  
      \_id: user.\_id,  
      name: user.name,  
      email: user.email,  
      role: user.role,  
      token: generateToken(user.\_id)  
    });

  } catch (error) {  
    next(error);  
  }

};

export const loginUser \= async (req, res, next) \=\> {

  try {

    const { email, password } \= req.body;

    const user \= await User.findOne({ email });

    if (user && (await user.matchPassword(password))) {

      res.json({  
        success: true,  
        \_id: user.\_id,  
        name: user.name,  
        email: user.email,  
        role: user.role,  
        token: generateToken(user.\_id)  
      });

    } else {

      res.status(412);  
      throw new Error('Invalid authentication credentials');

    }

  } catch (error) {  
    next(error);  
  }

};

export const getUserProfile \= async (req, res, next) \=\> {

  try {

    const user \= await User.findById(req.user.\_id);

    if (user) {

      res.json({  
        success: true,  
        user  
      });

    } else {

      res.status(404);  
      throw new Error('User context missing');

    }

  } catch (error) {  
    next(error);  
  }

};

---

# **Frontend Implementation (React \+ Tailwind CSS)**

## **Redux Cart Slice**

### **frontend/src/redux/cartSlice.js**

import { createSlice } from '@reduxjs/toolkit';

const initialState \= {

  cartItems: localStorage.getItem('cartItems')  
    ? JSON.parse(localStorage.getItem('cartItems'))  
    : \[\],

  deliveryFee: 5.00,

};

const cartSlice \= createSlice({

  name: 'cart',

  initialState,

  reducers: {

    addToCart: (state, action) \=\> {

      const existingItem \= state.cartItems.find(  
        item \=\> item.\_id \=== action.payload.\_id  
      );

      if (existingItem) {  
        existingItem.quantity \+= 1;  
      } else {  
        state.cartItems.push({  
          ...action.payload,  
          quantity: 1  
        });  
      }

      localStorage.setItem(  
        'cartItems',  
        JSON.stringify(state.cartItems)  
      );

    },

    decreaseQuantity: (state, action) \=\> {

      const item \= state.cartItems.find(  
        item \=\> item.\_id \=== action.payload  
      );

      if (item && item.quantity \> 1\) {  
        item.quantity \-= 1;  
      } else {  
        state.cartItems \= state.cartItems.filter(  
          item \=\> item.\_id \!== action.payload  
        );  
      }

      localStorage.setItem(  
        'cartItems',  
        JSON.stringify(state.cartItems)  
      );

    },

    removeFromCart: (state, action) \=\> {

      state.cartItems \= state.cartItems.filter(  
        item \=\> item.\_id \!== action.payload  
      );

      localStorage.setItem(  
        'cartItems',  
        JSON.stringify(state.cartItems)  
      );

    },

    clearCart: (state) \=\> {

      state.cartItems \= \[\];

      localStorage.removeItem('cartItems');

    }

  }

});

export const {  
  addToCart,  
  decreaseQuantity,  
  removeFromCart,  
  clearCart  
} \= cartSlice.actions;

export default cartSlice.reducer;

---

# **Authentication Context**

## **frontend/src/context/AuthContext.jsx**

import React, {  
  createContext,  
  useState,  
  useEffect  
} from 'react';

export const AuthContext \= createContext();

export const AuthProvider \= ({ children }) \=\> {

  const \[user, setUser\] \= useState(null);

  const \[token, setToken\] \= useState(  
    localStorage.getItem('token') || ''  
  );

  useEffect(() \=\> {

    if (token) {

      const savedUser \= localStorage.getItem('user');

      if (savedUser) {  
        setUser(JSON.parse(savedUser));  
      }

    }

  }, \[token\]);

  const login \= (userData, userToken) \=\> {

    setUser(userData);  
    setToken(userToken);

    localStorage.setItem('token', userToken);

    localStorage.setItem(  
      'user',  
      JSON.stringify(userData)  
    );

  };

  const logout \= () \=\> {

    setUser(null);  
    setToken('');

    localStorage.removeItem('token');  
    localStorage.removeItem('user');

  };

  return (

    \<AuthContext.Provider  
      value={{  
        user,  
        token,  
        login,  
        logout,  
        isAdmin: user?.role \=== 'admin'  
      }}  
    \>  
      {children}  
    \</AuthContext.Provider\>

  );

};

---

# **Navbar Component**

## **frontend/src/components/Navbar.jsx**

import React, { useContext } from 'react';

import {  
  Link,  
  useNavigate  
} from 'react-router-dom';

import { useSelector } from 'react-redux';

import { AuthContext } from '../context/AuthContext';

export default function Navbar() {

  const { user, logout, isAdmin } \=  
    useContext(AuthContext);

  const { cartItems } \= useSelector(  
    (state) \=\> state.cart  
  );

  const navigate \= useNavigate();

  const handleLogout \= () \=\> {

    logout();  
    navigate('/login');

  };

  return (

    \<nav className="bg-slate-900 text-white shadow-md sticky top-0 z-50 px-6 py-4 flex justify-between items-center"\>

      \<Link  
        to="/"  
        className="text-2xl font-bold tracking-tight text-orange-500"  
      \>  
        BiteExpress  
      \</Link\>

      \<div className="flex items-center space-x-6 font-medium"\>

        \<Link  
          to="/"  
          className="hover:text-orange-400 transition"  
        \>  
          Menu  
        \</Link\>

        {user && \!isAdmin && (  
          \<Link  
            to="/my-orders"  
            className="hover:text-orange-400 transition"  
          \>  
            My Orders  
          \</Link\>  
        )}

        {isAdmin && (  
          \<Link  
            to="/admin/dashboard"  
            className="bg-red-600 px-3 py-1 rounded text-sm hover:bg-red-700"  
          \>  
            Admin Panel  
          \</Link\>  
        )}

        \<Link  
          to="/cart"  
          className="relative flex items-center space-x-1 hover:text-orange-400 transition"  
        \>

          \<span\>Cart\</span\>

          \<span className="bg-orange-500 text-xs font-bold rounded-full w-5 h-5 flex items-center justify-center"\>

            {cartItems.reduce(  
              (acc, obj) \=\> acc \+ obj.quantity,  
              0  
            )}

          \</span\>

        \</Link\>

        {user ? (

          \<button  
            onClick={handleLogout}  
            className="border border-orange-500 text-orange-500 px-4 py-1.5 rounded-lg hover:bg-orange-500 hover:text-white transition"  
          \>  
            Logout  
          \</button\>

        ) : (

          \<Link  
            to="/login"  
            className="bg-orange-500 text-white px-4 py-1.5 rounded-lg hover:bg-orange-600 transition"  
          \>  
            Login  
          \</Link\>

        )}

      \</div\>

    \</nav\>

  );

}

---

# **Setup & Deployment**

## **Run Backend**

cd backend

npm install

npm run dev

---

## **Run Frontend**

cd frontend

npm install

npm run dev

---

# **Production Deployment**

## **Backend Deployment**

Deploy backend to:

* Render  
* Railway

Environment Variables:

MONGO\_URI=  
JWT\_SECRET=  
NODE\_ENV=production

---

## **Frontend Deployment**

Deploy frontend to:

* Vercel  
* Netlify

Update Axios API URLs from:

http://localhost:5000

to your deployed backend domain.

Build command:

npm run build

Output directory:

dist

---

# **Final Features Included**

✅ JWT Authentication  
✅ Role-Based Authorization  
✅ Redux Cart System  
✅ Admin Dashboard  
✅ Order Management  
✅ Secure Password Hashing  
✅ MongoDB Aggregations  
✅ Responsive Tailwind UI  
✅ RESTful API Architecture  
✅ Production Deployment Ready  
✅ Rate Limiting & Security Middleware  
✅ Scalable Folder Structure  
✅ Persistent Login Sessions  
✅ Fully Modular MERN Stack Architecture

**Ratings & Evaluations (RLHF)**

Dimension 1: Correctness — 3/5  
The backend structure, Mongoose models, JWT auth, password hashing, and Redux cart logic are mostly correct. However, the response claims MongoDB aggregations, rate limiting, and security middleware are included, but actual implementation is missing or incomplete. Also, frontend routing, API calls, checkout logic, order controllers, food controllers, admin controllers, and store setup are not actually provided.

Dimension 2: Relevance — 3/5  
The answer is relevant to a MERN food order management website. It covers backend, frontend, authentication, cart, admin structure, MongoDB, and deployment. But it does not fully implement all promised modules like order placement, food management, admin dashboard, and payment flow.

Dimension 3: Completeness — 2/5  
The response looks “production-ready” in title, but many key files are only listed, not implemented. Missing major parts include server.js, routes, food/order/admin controllers, React pages, Redux store, protected route, checkout flow, API integration with Axios/fetch, and admin dashboard logic. So it is more of a strong starter architecture than a complete project.

Dimension 4: Style & Presentation — 4/5  
Presentation is clean, readable, and well-organized. The folder structure is clear, code blocks are separated properly, and the flow from backend to frontend to deployment is easy to follow.

Dimension 5: Coherence — 3/5  
The overall structure is coherent and logically arranged. However, some final feature claims do not match the actual code shown, for example “MongoDB Aggregations,” “Rate Limiting,” and “Fully Modular” are claimed without real implementation.

Dimension 6: Helpfulness — 3/5  
Helpful as a blueprint or partial starter code. A developer can understand the architecture and start building from it, but cannot run the full app end-to-end because many required files and integrations are missing.

Dimension 7: Creativity — 3/5  
The architecture is standard but practical. Role-based admin access, modular backend folders, Redux cart persistence, and deployment notes are useful, but there is no advanced feature like live order tracking, payment gateway, image upload, search/filter, coupon system, or analytics.

# Likert Score \- 2

## **Final Verdict**

Response A is better than Response B. Response A gives a more complete MERN food-ordering implementation because it includes actual backend flow like server.js, MongoDB connection, JWT generator, auth controller, food controller, order controller, routes, Axios setup, cart context, food page, cart page, and an admin dashboard skeleton.Response B is clean and well-organized, but it leaves many promised parts unimplemented, including food/order/admin controllers, routes, checkout flow, admin dashboard logic, order management, and API integration. It also claims features like MongoDB Aggregations, Rate Limiting & Security Middleware, and Admin Dashboard, but these are not actually fully shown in the code.

