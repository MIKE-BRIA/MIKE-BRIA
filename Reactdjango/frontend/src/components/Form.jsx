import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

const Form = ({ route, method }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const name = method === "login" ? "Login" : "Register";

  // const handleSubmit = async (e) => {
  //   setLoading(true);
  //   e.preventDefault();

  //   try {
  //     const res = await api.post(route, { username, password });
  //     if (method === "login") {
  //       localStorage.setItem(ACCESS_TOKEN, res.data.access);
  //       localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
  //       navigate("/");
  //     } else {
  //       navigate("/login");
  //     }
  //   } catch (error) {
  //     alert(error);
  //   } finally {
  //     setLoading(false);
  //   }
  // };

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();

    try {
      const res = await api.post(route, { username, password });
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        navigate("/");
      } else {
        navigate("/login");
      }
    } catch (error) {
      if (error.response) {
        // The request was made and the server responded with a status code
        // that falls out of the range of 2xx
        alert(
          error.response.data.detail || "An error occurred. Please try again."
        );
      } else if (error.request) {
        // The request was made but no response was received
        alert(
          "No response from the server. Please check your network connection."
        );
      } else {
        // Something happened in setting up the request that triggered an error
        alert("An unexpected error occurred. Please try again.");
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>{name}</h1>
      <input
        type="text"
        className="form-input"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Enter Username"
      />
      <input
        type="password"
        className="form-input"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Enter Password"
      />
      {loading && <LoadingIndicator />}
      <button className="form-button" type="submit">
        {name}
      </button>
    </form>
  );
};

export default Form;
