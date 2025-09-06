import React, { useEffect, useState } from "react";
import { api } from "../api";

const Profile = () => {
  const [student, setStudent] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchProfile = async () => {
      try {
        const response = await api.get("/students/me");
        setStudent(response.data);
      } catch (err) {
        setError(err.response?.data?.detail || "Failed to load profile");
      }
    };
    fetchProfile();
  }, []);

  if (error) return <p className="text-red-500 text-center mt-10">{error}</p>;
  if (!student) return <p className="text-center mt-10">Loading...</p>;

  return (
    <div className="max-w-xl mx-auto mt-10 p-4 bg-white rounded shadow">
      <h1 className="text-2xl font-bold mb-4">Student Profile</h1>
      <p><strong>Name:</strong> {student.name}</p>
      <p><strong>Matric No:</strong> {student.matric_no}</p>
      <p><strong>Program:</strong> {student.program}</p>
      <p><strong>Level:</strong> {student.level}</p>
      <p><strong>Session:</strong> {student.session}</p>
    </div>
  );
};

export default Profile;
