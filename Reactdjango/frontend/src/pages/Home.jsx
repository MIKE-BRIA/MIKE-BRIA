import React from "react";
import { useState } from "react";
import api from "../api";
import { useEffect } from "react";
import Note from "../components/Note";
import "../styles/Home.css";

const Home = () => {
  const [notes, setNotes] = useState([]);
  const [content, setContent] = useState("");
  const [title, setTitle] = useState("");

  useEffect(() => {
    getNotes();
  }, []);

  const getNotes = () => {
    api
      .get("/api/notes/")
      .then((res) => res.data)
      .then((data) => {
        setNotes(data);
        console.log(data);
      })
      .catch((error) => alert(error));
  };

  const deleteNote = (id) => {
    api
      .delete(`/api/notes/delete/${id}/`)
      .then((res) => {
        if (res.status === 204) alert("Note deleted!");
        else alert("Failed to delete Note");
        getNotes();
      })
      .catch((error) => alert(error));
  };

  const createNote = async (e) => {
    e.preventDefault();

    try {
      const res = await api.post("/api/notes/", { content, title });
      console.log(res); // Inspect the response structure

      if (res.status === 201) {
        alert("Note Created!");
      } else {
        alert("Failed to make note.");
      }
    } catch (error) {
      alert(`Error: ${error.message || "Something went wrong!"}`);
    } finally {
      getNotes();
    }
  };

  return (
    <div>
      <div>
        <h2>Notes</h2>

        {notes.map((note) => (
          <Note key={note.id} note={note} onDelete={deleteNote} />
        ))}
      </div>
      <h2>Create a Note</h2>

      <form onSubmit={createNote}>
        <label htmlFor="title">Title:</label>
        <br />
        <input
          type="text"
          id="title"
          name="title"
          required
          onChange={(e) => setTitle(e.target.value)}
        />
        <br />
        <label htmlFor="content">Content:</label>
        <br />
        <textarea
          name="content"
          id="content"
          required
          value={content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
        <br />
        <input type="submit" value={"submit"} />
      </form>
    </div>
  );
};

export default Home;
