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