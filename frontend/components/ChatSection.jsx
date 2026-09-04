import { useState } from "react";
import styles from "./ChatSection.module.css";
import { Send } from "lucide-react";
import { useDispatch } from "react-redux";
import {
  addMessage,
  changeStatus,
} from "../slice/chatHistory";
import Chat from "./Chat";

export default function ChatSection() {
  const dispatch = useDispatch();

  const [query, setQuery] = useState("");

  const handleChange = (e) => {
    setQuery(e.target.value);
  };

  const handleFormSubmit = (e) => {
    e.preventDefault();

    if (!query.trim()) {
      return;
    }

    const userQuery = {
      role: "user",
      content: query,
    };

    dispatch(addMessage(userQuery));
    dispatch(changeStatus(true));

    async function sendingQuery() {
      try {
        const response = await fetch(
          "http://localhost:8000/chat",
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify({
              message: query,
            }),
          }
        );

        if (!response.ok) {
          throw new Error("Failed to get response");
        }

        const data = await response.json();

        const assistantResponse = {
          role: "assistant",
          content: data,
        };

        dispatch(addMessage(assistantResponse));

        setQuery("");
      } catch (error) {
        console.error(
          "Error fetching assistant response:",
          error
        );
      } finally {
        dispatch(changeStatus(false));
      }
    }

    sendingQuery();
  };

  return (
    <div className={styles.container}>
      <Chat />

      <form
        onSubmit={handleFormSubmit}
        className={styles.form}
      >
        <textarea
          value={query}
          className={styles.input}
          placeholder="Ask me anything about his skills, projects, experience, or education."
          rows="3"
          onChange={handleChange}
        />

        <div className={styles.actions}>
          <button
            type="submit"
            className={styles.send}
            disabled={!query.trim()}
          >
            <Send
              className={styles.sendIcon}
              size={20}
            />
          </button>
        </div>
      </form>

      <p className={styles.disclaimer}>
        An AI powered Chatbot made by Gautam for Gautam.
      </p>
    </div>
  );
}