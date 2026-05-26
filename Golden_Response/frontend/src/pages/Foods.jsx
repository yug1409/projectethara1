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