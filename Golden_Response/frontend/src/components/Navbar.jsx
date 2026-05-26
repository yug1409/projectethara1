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