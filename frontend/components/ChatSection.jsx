import { useState } from "react";
import styles from "./ChatSection.module.css";
import { Send } from "lucide-react";
import { useDispatch } from "react-redux";
import { addMessage, changeStatus } from "../slice/chatHistory";
import Chat from "./Chat";

export default function ChatSection() {
  const dispatch = useDispatch();
  const [query, setQuery] = useState("");

  const handleChange = function (e) {
    setQuery(e.target.value);
  };

  const handleFormSubmit = function (e) {
    e.preventDefault();

    const userQuery = {
      role: "user",
      content: query,
    };

    dispatch(addMessage(userQuery));
    dispatch(changeStatus(true));

    async function sendingQuery() {
      try {
        const response = await fetch("http://localhost:8000/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: query }),
        });
        const data = await response.json();

        const assistantResponse = {
          role: "assistant",
          content: data,
        };
        dispatch(addMessage(assistantResponse));
        setQuery("");
      } catch (error) {
        console.error("Error fetching assistant response:", error);
      } finally {
        dispatch(changeStatus(false));
      }
    }

    sendingQuery(); // <-- Moved inside handleFormSubmit
  };

  return (
    <div className={styles.container}>
      
      <Chat />


      <form onSubmit={(e) => handleFormSubmit(e)} className={styles.form}>
        <textarea
          value={query}
          className={styles.input}
          placeholder="Ask me anything..."
          rows="3"
          onChange={(e) => handleChange(e)}
        />

        <div className={styles.actions}>
          <button type="submit" className={styles.send}>
            <Send className={styles.sendIcon} size={20} />
          </button>
        </div>
      </form>

      <p className={styles.disclaimer}>
        An AI powered Chatbot made by Gautam for Gautam.
      </p>
    </div>
  );
}