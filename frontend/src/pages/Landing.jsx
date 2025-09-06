import React from "react";
import { Link } from "react-router-dom";

const Landing = () => {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-gray-100">
      <h1 className="text-4xl font-bold mb-4">Welcome to STC Student Portal</h1>
      <p className="mb-6 text-gray-700">Manage your profile and track your academic records seamlessly.</p>
      <div className="space-x-4">
        <Link to="/login" className="px-4 py-2 bg-blue-600 text-white rounded">Login</Link>
        <Link to="/register" className="px-4 py-2 bg-green-600 text-white rounded">Register</Link>
      </div>
    </div>
  );
};

export default Landing;
