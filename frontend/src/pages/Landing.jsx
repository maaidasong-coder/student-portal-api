import React from "react";
import { Link } from "react-router-dom";

const Landing = () => {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-4">
      <h1 className="text-5xl font-extrabold mb-6 text-center text-gray-900">
        Welcome to STC Student Portal
      </h1>
      <p className="mb-8 text-center text-gray-700 max-w-xl">
        Manage your profile and track your academic records seamlessly. Access your personal dashboard and stay updated with your academic progress.
      </p>
      <div className="flex space-x-4">
        <Link
          to="/login"
          className="px-6 py-3 bg-blue-600 hover:bg-blue-700 transition text-white font-semibold rounded shadow"
        >
          Login
        </Link>
        <Link
          to="/register"
          className="px-6 py-3 bg-green-600 hover:bg-green-700 transition text-white font-semibold rounded shadow"
        >
          Register
        </Link>
      </div>
    </div>
  );
};

export default Landing;
