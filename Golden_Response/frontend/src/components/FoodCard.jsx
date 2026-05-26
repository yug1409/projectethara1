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