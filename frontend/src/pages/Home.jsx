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