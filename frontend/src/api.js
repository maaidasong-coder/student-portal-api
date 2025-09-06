import axios from "axios";

const API_URL = "https://student-portal-api-c04l.onrender.com";

export const api = axios.create({
  baseURL: API_URL,
});

// Add JWT token automatically to requests if present
api.interceptors.request.use(config => {
  const token = localStorage.getItem("token");
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});
