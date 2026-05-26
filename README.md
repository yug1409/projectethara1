
# Food Order Management Website — MERN Stack

A full-stack Food Order Management System built using the MERN stack.  
It supports customer authentication, food browsing, cart management, order placement, and basic admin order/food management flow.

---
---

## Project Structure

```text
food-order-management/
│
├── backend/
│   ├── config/
│   │   └── db.js
│   │
│   ├── controllers/
│   │   ├── authController.js
│   │   ├── foodController.js
│   │   └── orderController.js
│   │
│   ├── middleware/
│   │   └── authMiddleware.js
│   │
│   ├── models/
│   │   ├── Food.js
│   │   ├── Order.js
│   │   └── User.js
│   │
│   ├── routes/
│   │   ├── authRoutes.js
│   │   ├── foodRoutes.js
│   │   └── orderRoutes.js
│   │
│   ├── utils/
│   │   └── generateToken.js
│   │
│   ├── .env
│   ├── package-lock.json
│   └── package.json
│
├── frontend/
│   ├── node_modules/
│   ├── public/
│   │
│   ├── src/
│   │   ├── api/
│   │   │   └── axios.js
│   │   │
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   ├── AdminRoute.jsx
│   │   │   ├── FoodCard.jsx
│   │   │   ├── Navbar.jsx
│   │   │   └── ProtectedRoute.jsx
│   │   │
│   │   ├── context/
│   │   │   ├── AuthContext.jsx
│   │   │   └── CartContext.jsx
│   │   │
│   │   ├── pages/
│   │   │   ├── AdminDashboard.jsx
│   │   │   ├── Cart.jsx
│   │   │   ├── Checkout.jsx
│   │   │   ├── Foods.jsx
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── MyOrders.jsx
│   │   │   └── Register.jsx
│   │   │
│   │   ├── App.css
│   │   ├── App.jsx
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── .gitignore
│   ├── eslint.config.js
│   ├── index.html
│   ├── package.json
│   ├── README.md
│   └── vite.config.js
````

---
## Tech Stack

### Frontend
- React.js
- React Router
- Axios
- Context API
- Tailwind CSS

### Backend
- Node.js
- Express.js
- MongoDB
- Mongoose
- JWT Authentication
- bcrypt.js
- express-rate-limit

---

## Features

### Customer Features
- User registration
- User login
- JWT-based authentication
- Browse available food items
- Add food items to cart
- Remove items from cart
- View total cart amount
- Proceed to checkout
- Place food orders
- View personal order history

### Admin Features
- Admin-protected routes
- Add food items
- Update food items
- Delete food items
- View all orders
- Update order status
- Basic admin dashboard


## Backend Setup

### 1. Go to backend folder

```bash
cd backend
```

### 2. Install dependencies

```bash
npm init -y
npm install express mongoose dotenv cors bcryptjs jsonwebtoken express-rate-limit
npm install nodemon --save-dev
```

### 3. Create `.env` file

```env
PORT=5000
MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/food-order-db
JWT_SECRET=your_jwt_secret_key
NODE_ENV=development
```

### 4. Start backend server

```bash
npm run dev
```

Backend will run on:

```text
http://localhost:5000
```

---

## Frontend Setup

### 1. Go to frontend folder

```bash
cd frontend
```

### 2. Create React app using Vite

```bash
npm create vite@latest
```

### 3. Install dependencies

```bash
npm install
npm install axios react-router-dom
npm install -D tailwindcss postcss autoprefixer
```

### 4. Start frontend server

```bash
npm run dev
```

Frontend will run on:

```text
http://localhost:5173
```

---

## API Endpoints

### Auth Routes

| Method | Endpoint             | Description       |
| ------ | -------------------- | ----------------- |
| POST   | `/api/auth/register` | Register new user |
| POST   | `/api/auth/login`    | Login user        |

### Food Routes

| Method | Endpoint         | Description             | Access |
| ------ | ---------------- | ----------------------- | ------ |
| GET    | `/api/foods`     | Get all available foods | Public |
| POST   | `/api/foods`     | Create food item        | Admin  |
| PUT    | `/api/foods/:id` | Update food item        | Admin  |
| DELETE | `/api/foods/:id` | Delete food item        | Admin  |

### Order Routes

| Method | Endpoint                 | Description                 | Access |
| ------ | ------------------------ | --------------------------- | ------ |
| POST   | `/api/orders`            | Place order                 | User   |
| GET    | `/api/orders/my-orders`  | Get logged-in user's orders | User   |
| GET    | `/api/orders`            | Get all orders              | Admin  |
| PUT    | `/api/orders/:id/status` | Update order status         | Admin  |

---

## Application Flow

```text
1. User registers or logs in.
2. JWT token is generated and stored.
3. User browses available food items.
4. User adds food items to cart.
5. Cart calculates total amount.
6. User places order.
7. Backend verifies JWT token.
8. Order is stored in MongoDB.
9. Admin views all orders.
10. Admin updates order status.
11. User tracks order status from order history.
```

---

## Deployment

### Frontend Deployment

Frontend can be deployed on:

* Vercel
* Netlify

Before deployment, update API base URL in:

```js
frontend/src/api/axios.js
```

Change:

```js
baseURL: "http://localhost:5000/api"
```

To your deployed backend URL:

```js
baseURL: "https://your-backend-domain.com/api"
```

### Backend Deployment

Backend can be deployed on:

* Render
* Railway
* Cyclic

Add these environment variables in the hosting dashboard:

```env
MONGO_URI=
JWT_SECRET=
NODE_ENV=production
```

### Database

Use MongoDB Atlas for production database hosting.

---

## Future Improvements

* Payment gateway integration
* Food image upload using Cloudinary
* Email notification after order placement
* Live order tracking
* Coupon and discount system
* Admin analytics dashboard
* Search and filter food items
* Socket.io real-time order updates

---

## Conclusion

This project provides a strong MERN stack foundation for a food order management system.
It includes authentication, food browsing, cart handling, order placement, admin access, and deployment guidance.

The project is suitable as a starter full-stack application and can be extended into a production-ready food delivery platform.

```
```
