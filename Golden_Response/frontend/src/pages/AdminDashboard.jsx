// src/pages/AdminDashboard.jsx

const AdminDashboard = () => {
  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold">Admin Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mt-6">
        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Orders</h2>
          <p className="text-2xl font-bold">120</p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Foods</h2>
          <p className="text-2xl font-bold">45</p>
        </div>

        <div className="bg-white shadow p-6 rounded-xl">
          <h2>Total Users</h2>
          <p className="text-2xl font-bold">300</p>
        </div>
      </div>
    </div>
  );
};

export default AdminDashboard;