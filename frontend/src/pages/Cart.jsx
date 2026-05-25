// src/pages/Cart.jsx

import { useCart } from "../context/CartContext";
import { Link } from "react-router-dom";

const Cart = () => {
  const { cartItems, removeFromCart, totalAmount } = useCart();

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold">Your Cart</h1>

      {cartItems.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          {cartItems.map((item) => (
            <div
              key={item._id}
              className="flex justify-between items-center border-b py-4"
            >
              <div>
                <h3>{item.name}</h3>
                <p>
                  ₹{item.price} x {item.quantity}
                </p>
              </div>

              <button
                onClick={() => removeFromCart(item._id)}
                className="text-red-500"
              >
                Remove
              </button>
            </div>
          ))}

          <h2 className="text-xl font-bold mt-4">
            Total: ₹{totalAmount}
          </h2>

          <Link
            to="/checkout"
            className="inline-block mt-4 bg-green-600 text-white px-4 py-2 rounded"
          >
            Proceed to Checkout
          </Link>
        </>
      )}
    </div>
  );
};

export default Cart;