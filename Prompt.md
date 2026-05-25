                                                           **Food Order Management**

**Prompt**

**Context and Role**

You are a Full stack MERN Developer. Design and implement a complete Food Order Management website using the MERN.

The website should allow customers to browse food items, can add items to cart, place order and track order status. It must include an admin panel where restaurant staff should be able to manage food items, view order, update order status and manage users.

The application should be production ready ,responsive, secure, scalable, and fully functional from backend to frontend.

---

**Objective**

Develop a complete full-stack Food Order Management System that :

* Allow users to register and login securely.  
* Display food items with categories ,prices, images, and descriptions.  
* Allow users to add or remove food items from cart.  
* Allow users to place food orders.  
* Stores orders in MongoDB.  
* Gives an admin dashboard for managing food items and orders.  
* Support order status updates such as Pending ,Preparing, Out for Delivery, and Delivered.  
* Includes secure authentication and authorization.  
* Provides a clean , responsive, and user-friendly UI.

---

**Frontend Requirement  :**

React.js for frontend

The frontend must include:

* Home page with food categories and featured dishes.  
* Food listing page.  
* Food details page.  
* Cart page.  
* Checkout page.  
* Login and Register pages.  
* User order history page.  
* Admin dashboard.  
* Admin food management page.  
* Admin order management page.

The UI must be:

* Fully responsive for mobile ,tablet, and desktop.  
* Clean and modern.  
* Easy to navigate.  
* Built using reusable react components.  
* Styled using tailwind CSS or bootstrap

---

**User Authentication Requirements**

Implement secure authentication using:

* JWT token-based authentication.  
* bcrypt for password hashing.  
* Login and registration system.  
* Protected routes for logged-in users.  
* Admin-only protected routes.

User roles must include:

* Customer  
* Admin

Customers can:

* View food items.  
* Add items to cart.  
* Place orders.  
* View their own orders.

Admin can:

* Add new food items.  
* Edit food items.  
* Delete food items.  
* View all orders.  
* Update order status.  
* Manage users if required.

---

**Food Management Requirements**

Food items must include:

* Food name  
* Description  
* Price  
* Category  
* Image  
* Availability status  
* Created date

Admin should be able to:

* Add food items.  
* Edit food item.  
* Delete food items.  
* Mark food as available/unavailable.

Frontend should show:

* Food image  
* Name  
* Price  
* Category  
* Add to cart button  
* Food details

---

**Cart Requirements**

The cart system must allow users to:

* The cart system must allow users to:  
* Add food items into the cart.  
* Increase or decrease the quantity.  
* Remove items from cart.  
* View total price.  
* Proceed to checkout.


Cart must calculate:

* Item subtotal  
* Total amount  
* Delivery charges if required  
* Final payable amount

---

**Order Management Requirements**

When a user places an order , store the order in MongoDB with:

* User ID  
* Customer name  
* Food items  
* Quantity  
* Total amount  
* Delivery address  
* Phone number  
* Payment method  
* Order status  
* Order date and time  
* Order status should include:  
* Pending  
* Confirmed  
* Preparing  
* Out for Delivery  
* Delivered  
* Cancelled

Admin must be able to update order status from the dashboard.

---

**Backend Requirements**

Use **Node.js+Express.js** for backend.

Backend must include:

* REST APIs for authentication.  
* REST APIs for food items.  
* REST APIs for cart/order management.  
* REST APIs for admin actions.  
* MongoDB database connection.  
* Mongoose models.  
* Middleware for authentication and authorization.  
* Proper error handling.  
* Secure environment variables using dotenv


**API Requirements**

Create APIs for:

**Authentication**

* Post  /api/auth/register  
* Post  /api/auth/login  
* Get  /api/auth/profile

**Food**

* Get  /api/foods  
* Get  /api/foods/:id  
* Post  /api/foods  
* Put  /api/foods/:id  
* Delete  /api/foods/:id

**Orders**

* Post  /api/orders  
* Get  /api/orders/my-orders  
* Get  /api/orders  
* Put  /api/orders/:id/status

**Admin**

* Get  /api/admin/dashboard  
* Get  /api/admin/users  
* Delete  /api/admin/users/:id

---

**Database Requirements**

Use **MongoDB** with Mongoose.

Create models for:

**User Model**

* name  
* email  
* password  
* role  
* phone  
* address  
* createdAt

**Food Model**

* name  
* description  
* price  
* category  
* image  
* isAvailable  
* createdAt

**Order Model**

* user  
* items  
* totalAmount  
* deliveryAddress  
* phone  
* paymentMethod  
* orderStatus  
* createdAt

---

**Validation and Security Requirements**

The application must include:

* Input validation on frontend and backend.  
* bcrypt for password hashing.  
* JWT authentication.  
* Role-based authorization.  
* Secure API routes.  
* Environment variables for secret keys.  
* Sanitization to prevent XSS and injection attacks.  
* Proper CORS configuration.  
* Rate limiting for login APIs.  
* Structured JSON error responses.

---

**Error Handling Requirements**

Handle errors gracefully for:

* Handle errors gracefully for:  
* Invalid login credentials.  
* Duplicate email registration.  
* Missing required fields.  
* Invalid food item ID.  
* Empty cart checkout.  
* Unauthorized access.  
* Admin-only access violation.  
* Database connection errors.  
* Server errors.

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

**Performance and Scalability Requirement :**

Ensure that \-

* Frontend components are reusable.  
* API calls are optimized.  
* Loading states are shown.  
* Images are optimized.  
* MongoDB queries are efficient.  
* Backend can handle multiple users.  
* Code is modular and maintainable.  
* Admin dashboard loads data efficiently.  
* The app can be deployed on platforms like Vercel , Render, Railway, or Netlify.

---

**Technology Stack**

Use the following technologies:

**Frontend**

* React.js  
* React Router  
* Axios  
* Tailwind CSS or Bootstrap  
* Context API or Redux Toolkit for state management

**Backend**

* Node.js  
* Express.js  
* MongoDB  
* Mongoose  
* JWT  
* bcrypt  
* dotenv  
* cors  
* express-rate-limit

**Optional**

* Cloudinary for food image upload  
* Stripe or Razorpay for payment integration  
* Nodemailer for order confirmation emails  
* Redux Toolkit for cart state  
* Toast notifications for success/error messages

---

 

