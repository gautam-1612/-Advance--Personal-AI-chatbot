import { useState } from "react";
import styles from "./ChatSection.module.css";
import { Send } from "lucide-react";

export default function ChatSection() {

  const [query, setQuery] = useState("");

  const handleChange = function(e) {
    setQuery(e.target.value);
  }

  const handleFormSubmit = function(e) {
    e.preventDefault();
    
    async function sendingQuery() {
    const response = await fetch("http://localhost:8000/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: query })
    })

    const data = await response.json();
    console.log(data)
    setQuery("");
    }
    sendingQuery();
  }

  return (
    <div className={styles.container}>

      <div className={styles.emptyChat}>
        <p>Hi! I'm Gautam's AI assistant.</p>
        <p>Ask me anything about his skills, projects, experience, or education.</p>
      </div>

      <form onSubmit={(e) => handleFormSubmit(e)} className={styles.form}>
        <textarea
          value={query}
          className={styles.input}
          placeholder="Ask me anything..."
          rows="1"
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