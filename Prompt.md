**Prompt**

**Context and Role**

You are a Full Stack MERN Developer. Design and implement a complete Food Order Management website using the MERN stack.

The website should allow customers to browse food items ,add items to cart, place orders, and track order status. It must also include an admin panel where restaurant staff can manage food items ,view orders, update order status, and manage users.

The application should be production ready ,responsive, secure, scalable, and fully functional from backend to frontend. The response should not only give folder structure; it should provide working code, route logic, models, controllers, middleware, frontend pages ,setup steps, environment variables, and deployment guidance.

---

**Objective**

Develop a complete full stack Food Order Management System that:

* Allows users to register and login securely using JWT authentication and hashed passwords.  
* Displays food items with categories ,prices, images, descriptions, and availability status.  
* Allows users to add, remove, increase ,and decrease food item quantity in the cart.  
* Allows users to place food orders after providing delivery address, phone number , and payment method.  
* Stores all order details in MongoDB using proper Mongoose schemas.  
* Provides an admin dashboard for managing food items, orders , and users.  
* Supports order status updates such as Pending, Confirmed, Preparing, Out for Delivery, Delivered , and Cancelled.  
* Includes secure authentication and role based authorization for customer and admin.  
* Provides a clean , responsive, and user-friendly UI with proper loading, success, and error states.

---

**Frontend Requirement:**

Use React.js for the frontend.

The frontend must include:

* Home page with food categories , featured dishes, banner/hero section, and navigation to food listing.  
* Food listing page that displays all available food items with search, category filter, price ,image, and add-to-cart action.  
* Food details page that shows full description, image, price, category, availability, and add-to-cart button.  
* Cart page that shows selected items ,quantity controls, subtotal, delivery charge, and final payable amount.  
* Checkout page where users enter delivery address , phone number, payment method, and place the order.  
* Login and Register pages with form validation, error messages, and successful redirect after authentication.  
* User order history page where customers can see their previous orders and current order status.  
* Admin dashboard with summary cards such as total orders ,total users, total food items, and recent orders.  
* Admin food management page where admin can add, edit, delete ,and mark food items as available/unavailable.  
* Admin order management page where admin can view all orders and update their status.

The UI must be:

* Fully responsive for mobile, tablet ,and desktop.  
* Clean and modern with proper spacing , typography, colors, and buttons.  
* Easy to navigate with navbar, protected route handling, and clear page titles.  
* Built using reusable React components such as Navbar , FoodCard, Loader, ErrorMessage, ProtectedRoute ,AdminRoute , and FormInput.  
* Styled using Tailwind CSS or Bootstrap.  
* Able to show loading states during API calls and toast error messages when actions succeed/fail.

---

**User Authentication Requirements**

Implement secure authentication using:

* JWT token based authentication: generate token after login or register and send it in the Authorization header as `Bearer <token>`.  
* bcrypt password hashing:- never store plain text passwords in MongoDB.  
* Login and registration system: validate required fields ,duplicate email, password length, and invalid credentials.  
* Protected routes for logged-in users: checkout ,cart order placement, profile, and order history should require login.  
* Admin-only protected routes: food creation, food update ,food delete, all orders, status update, dashboard, and user management should only be accessible by admin users.

User roles must include:

* Customer  
* Admin

Customers can:

* View food items.  
* Add items to cart.  
* Place orders.  
* View only their own orders.  
* Track order status.

Admin can:

* Add new food items.  
* Edit food items.  
* Delete food items.  
* Mark food as available/unavailable.  
* View all orders from all users.  
* Update order status.  
* View users and delete/manage users if required.

---

**Food Management Requirements**

Food items must include:

* Food name: required string,minimum 2 characters.  
* Description: required string explaining the food item.  
* Price: required number, must be greater than 0\.  
* Category: required string such as Pizza ,Burger, Drinks, Dessert, Indian ,Chinese, etc.  
* Image: image URL or uploaded image path.  
* Availability status: boolean value to show whether an item is available for ordering.  
* Created date: automatically stored using timestamps.

Admin should be able to:

* Add food items with all required details.  
* Edit food item details such as name, price ,category, image, and availability.  
* Delete food items only through admin-protected API.  
* Mark food as available/unavailable without deleting the item.

Frontend should show:

* Food image.  
* Name.  
* Price.  
* Category.  
* Availability status.  
* Add to cart button only when food is available.  
* Food details page link.

---

Cart Requirements

The cart system must allow users to:

* Add food items into the cart.  
* Increase or decrease quantity.  
* Remove items from cart.  
* View total selected items.  
* View total price before checkout.  
* Proceed to checkout only if the cart is not empty.

Cart must calculate:

* Item subtotal: price × quantity for each food item.  
* Total amount: sum of all item subtotals.  
* Delivery charges if required.  
* Final payable amount: total amount \+ delivery charges.

The cart should persist during page refresh using Context API, Redux Toolkit, or localStorage. It should also clear automatically after successful order placement.

---

**Order Management Requirements**

When a user places an order, store the order in MongoDB with:

* User ID.  
* Customer name.  
* Food items with food ID, name ,price, and quantity.  
* Quantity for each item.  
* Total amount.  
* Delivery address.  
* Phone number.  
* Payment methods such as COD, Card ,UPI, Razorpay, or Stripe if implemented.  
* Order status.  
* Order date and time.

Order status should include:

* Pending  
* Confirmed  
* Preparing  
* Out for Delivery  
* Delivered  
* Cancelled

Admin must be able to update order status from the dashboard . Customers must only be able to view their own orders, while admin can view all orders.

## **Data Processing Requirements**

The system should properly process data from frontend to backend before storing it in the database.

### Authentication Processing

* Passwords should be hashed using bcrypt before storing in MongoDB.  
* JWT token should be generated after successful login or register.  
* JWT token should be verified for protected routes.

### Food Data Processing

* Food data should be validated before saving.  
* Category filtering and search should be processed efficiently.  
* Availability status should control whether users can order the item.

### Cart Processing

* Cart totals should be dynamically calculated.  
* Quantity updates should instantly update subtotal and total amount.  
* Cart data should persist using localStorage, Context API or Redux Toolkit.

### Order Processing

When an order is placed:

* Verify all food items exist.  
* Validate quantities and stock availability if implemented.  
* Calculate final total amount securely on backend.  
* Store order details in MongoDB.  
* Set default order status as `Pending`.  
* Clear cart after successful order placement.

---

**Backend Requirements**

Use Node.js+Express.js for backend.

Backend must include:

* REST APIs for authentication.  
* REST APIs for food items.  
* REST APIs for cart/order management.  
* REST APIs for admin actions.  
* MongoDB database connection using Mongoose.  
* Mongoose models for User, Food, and Order.  
* Middleware for authentication and authorization.  
* Proper error handling using centralized error middleware.  
* Secure environment variables using dotenv.  
* Clean folder structure with config ,models, controllers, routes, middleware, and utils folders.  
* Common response format for APIs, for example `{ success: true, data: ... }` and `{ success: false, message: ... }`.

---

**API Requirements**

Create APIs for:

Authentication

* Post `/api/auth/register`  
  * Purpose: Register a new customer.  
  * Required body: name, email, password, phone, address.  
  * Validation: email must be unique, password must be strong enough , required fields cannot be empty.  
  * Success response: return user details without password and JWT token.  
  * Error cases: duplicate email, missing fields, invalid email format , weak password.  
* Post `/api/auth/login`  
  * Purpose: Login existing user.  
  * Required body: email and password.  
  * Validation: email and password required.  
  * Success response: return user details ,role, and JWT token.  
  * Error cases: invalid credentials, user not found, wrong password, rate limit exceeded.  
* Get `/api/auth/profile`  
  * Purpose: Get logged-in user profile.  
  * Access: protected route.  
  * Success response: return logged-in user details without password.  
  * Error cases: missing token, invalid token , user not found.

Food

* Get `/api/foods`  
  * Purpose: Get all available food items.  
  * Access: public.  
  * Should support optional search/category filters if possible.  
  * Success response: list of food items.  
  * Error cases: server/database error.  
* Get `/api/foods/:id`  
  * Purpose: Get single food item details.  
  * Access: public.  
  * Validation: check if `id` is valid MongoDB ObjectId.  
  * Error cases: invalid ID, food not found.  
* Post `/api/foods`  
  * Purpose: Create a new food item.  
  * Access: admin only.  
  * Required body: name, description, price, category, image, isAvailable.  
  * Validation: price must be positive, required fields cannot be empty.  
  * Error cases: unauthorized user , non-admin access, validation failure.  
* Put `/api/foods/:id`  
  * Purpose: Update an existing food item.  
  * Access: admin only.  
  * Validation: valid food ID, valid updated fields.  
  * Error cases: invalid ID , food not found, unauthorized access.  
* Delete `/api/foods/:id`  
  * Purpose: Delete a food item.  
  * Access: admin only.  
  * Validation: valid food ID.  
  * Error cases: invalid ID , food not found, unauthorized access.

Orders

* Post `/api/orders`  
  * Purpose: Place a new order.  
  * Access: logged-in customer.  
  * Required body: items, totalAmount, deliveryAddress, phone, paymentMethod.  
  * Validation: cart/items cannot be empty ,quantity must be at least 1, delivery address and phone required.  
  * Success response: created order details.  
  * Error cases: empty cart , unavailable food item, invalid quantity, missing address, unauthorized user.  
* Get `/api/orders/my-orders`  
  * Purpose: Get logged-in user's order history.  
  * Access: logged-in customer.  
  * Success response: list of orders belonging only to the logged-in user.  
  * Error cases: missing token , invalid token, no orders found.  
* Get `/api/orders`  
  * Purpose: Get all orders.  
  * Access: admin only.  
  * Success response: all orders with user details populated.  
  * Error cases: unauthorized user , admin-only access violation.  
* Put `/api/orders/:id/status`  
  * Purpose: Update order status.  
  * Access: admin only.  
  * Required body: orderStatus.  
  * Validation: orderStatus must be one of Pending , Confirmed, Preparing, Out for Delivery, Delivered, Cancelled.  
  * Error cases: invalid order ID, order not found, invalid status, unauthorized access.

Admin

* Get `/api/admin/dashboard`  
  * Purpose: Return admin dashboard summary.  
  * Access: admin only.  
  * Response should include total users , total food items, total orders, pending orders, delivered orders, and recent orders.  
  * Error cases: unauthorized user, admin-only access violation, database error.  
* Get `/api/admin/users`  
  * Purpose: Get all registered users.  
  * Access: admin only.  
  * Response should not include user passwords.  
  * Error cases: unauthorized user , admin-only access violation.  
* Delete `/api/admin/users/:id`  
  * Purpose: Delete or deactivate a user.  
  * Access: admin only.  
  * Validation: valid user ID.  
  * Error cases: invalid user ID, user not found , admin trying to delete own account if restricted.

---

**Database Requirements**

Use MongoDB with Mongoose.

Create models for:

User Model

* name: required string.  
* email: required, unique , lowercase string.  
* password: required hashed string.  
* role: enum with customer/admin, default customer.  
* phone: string.  
* address: string.  
* createdAt: generated automatically with timestamps.

Food Model

* name: required string.  
* description: required string.  
* price: required number greater than 0\.  
* category: required string and should be indexed for faster filtering.  
* image: required string or URL.  
* isAvailable: boolean default true.  
* createdAt: generated automatically with timestamps.

Order Model

* user: ObjectId reference to User.  
* items: array containing food reference , name, price, quantity.  
* totalAmount: required number.  
* deliveryAddress: required string.  
* phone: required string.  
* paymentMethod: enum such as COD , Card, UPI, Razorpay.  
* orderStatus: enum with valid order statuses.  
* createdAt: generated automatically with timestamps.

---

**Validation and Security Requirements**

The application must include:

* Frontend validation: show clear messages before submitting forms, such as required name, invalid email, short password, invalid phone number , empty cart, and missing delivery address.  
* Backend validation: never trust frontend data; validate all request body fields again in controllers or middleware.  
* ObjectId validation: validate MongoDB IDs before calling `findById`, update, or delete APIs.  
* bcrypt password hashing: hash passwords before saving users; never return password in API response.  
* JWT authentication: verify token for protected routes and reject missing , expired, or invalid tokens.  
* Role-based authorization: allow admin APIs only when `req.user.role === "admin"`.  
* Secure API routes: protect order creation , user profile, order history, admin dashboard, food CRUD, and order status update.  
* Environment variables: store MongoDB URI, JWT secret, port, and third-party keys in `.env`; do not hardcode secrets in code.  
* Sanitization: sanitize user input to reduce XSS and injection attacks , especially name, description, address, and search query fields.  
* CORS configuration: allow only frontend domain in production and avoid using open CORS for deployed apps.  
* Rate limiting: apply rate limiting on login/register APIs to reduce brute force attacks.  
* Structured JSON error responses :every error should return a consistent shape like `{ success: false, message: "Error message" }`.  
* Security headers: use common Express security practices such as Helmet if included.  
* No sensitive logs: do not log passwords , JWT tokens, or full user private details.

---

**Error Handling Requirements**

Handle errors gracefully for:

* Invalid login credentials: return 401 with a safe message like “Invalid email or password.”  
* Duplicate email registration: return 400 with message “ User already exists.”  
* Missing required fields :return 400 and clearly mention which field is missing.  
* Invalid food item ID : return 400 if ID format is invalid and 404 if item does not exist.  
* Invalid order ID: return 400 for invalid ID and 404 for order not found.  
* Empty cart checkout: return 400 with message “Cart cannot be empty.”  
* Invalid order status: return 400 if admin sends a status outside the allowed enum.  
* Unauthorized access: return 401 when the token is missing , expired, or invalid.  
* Admin-only access violation: return 403 when a customer tries to access admin APIs.  
* Database connection errors: log internally and return a safe 500 response.  
* Server errors: use centralized error middleware and avoid exposing stack traces in production.  
* Frontend API errors : display user-friendly toast messages and avoid blank screens.  
* Network errors: show retry-friendly messages when the backend is unavailable.

Use proper HTTP status codes:

* 200 for successful fetch/update.  
* 201 for successful creation.  
* 400 for validation errors.  
* 401 for unauthenticated users.  
* 403 for forbidden/admin-only access.  
* 404 for resources not found.  
* 429 for too many requests.  
* 500 for server/database errors.

---

**Output Requirements**

The final output must include:

* Fully working MERN food order management website.  
* React frontend with responsive UI.  
* Node.js and Express backend.  
* MongoDB database integration.  
* JWT authentication.  
* Customer order flow.  
* Admin dashboard.  
* Food item CRUD operations.  
* Order status management.  
* Proper folder structure.  
* Setup instructions.  
* Environment variable configuration.  
* Deployment steps.  
* API testing examples using Postman/cURL if possible.  
* Explanation of how to run frontend and backend locally.

---

Performance and Scalability Requirement:

Ensure that:

* Frontend components are reusable and not duplicated unnecessarily.  
* API calls are optimized and not repeated unnecessarily.  
* Loading states are shown during API requests.  
* Images are optimized and use proper sizes.  
* MongoDB queries are efficient and use indexes where useful, such as category and user fields.  
* Backend can handle multiple users using stateless JWT authentication.  
* Code is modular and maintainable with separate controllers ,routes, models, middleware, and utilities.  
* Admin dashboard loads data efficiently using summary APIs rather than fetching unnecessary full data.  
* The app can be deployed on platforms like Vercel, Render ,Railway, or Netlify.  
* Avoid storing unnecessary large data in localStorage.  
* Use pagination or filtering for large food/order lists if possible.

---

**Technology Stack**

Use the following technologies:

Frontend

* React.js  
* React Router  
* Axios  
* Tailwind CSS or Bootstrap  
* Context API or Redux Toolkit for state management

Backend

* Node.js  
* Express.js  
* MongoDB  
* Mongoose  
* JWT  
* bcrypt  
* dotenv  
* cors  
* express-rate-limit

Optional

* Cloudinary for food image upload.  
* Stripe or Razorpay for payment integration.  
* Nodemailer for order confirmation emails.  
* Redux Toolkit for cart state.  
* Toast notifications for success/error messages.  
* Helmet for secure HTTP headers.  
* express-validator or Joi/Zod for request validation.

