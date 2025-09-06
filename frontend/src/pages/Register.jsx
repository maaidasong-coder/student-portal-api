import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../api";

const Register = () => {
  const navigate = useNavigate();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);
    try {
      // Register user
      await api.post("/auth/register", { email, password });

      // Optional: auto-login after registration
      const loginResponse = await api.post("/auth/login", { email, password });
      localStorage.setItem("token", loginResponse.data.access_token);

      // Redirect to profile
      navigate("/profile");
    } catch (err) {
      setError(err.response?.data?.detail || "Registration failed. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-4">
      <h1 className="text-4xl font-bold mb-6 text-center">Register</h1>
      <form onSubmit={handleRegister} className="flex flex-col space-y-4 w-full max-w-sm bg-white p-6 rounded shadow-md">
        <input
          type="email"
          placeholder="Email"
          className="p-3 border rounded focus:outline-none focus:ring-2 focus:ring-green-500"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          className="p-3 border rounded focus:outline-none focus:ring-2 focus:ring-green-500"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button
          type="submit"
          className={`bg-green-600 text-white p-3 rounded font-semibold ${loading ? "opacity-70 cursor-not-allowed" : "hover:bg-green-700"}`}
          disabled={loading}
        >
          {loading ? "Registering..." : "Register"}
        </button>
        {error && <p className="text-red-500 text-center">{error}</p>}
      </form>
    </div>
  );
};

export default Register;
