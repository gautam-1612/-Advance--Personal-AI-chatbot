import styles from "./Chat.module.css";
import { useSelector } from "react-redux";
import { useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function Chat() {
  const chatHistory = useSelector(
    (state) => state.chatHistory.chatHistory
  );

  const chatEndRef = useRef(null);
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [chatHistory]);

  const isLoading = useSelector(
    (state) => state.chatHistory.isLoading
  );

  return (
    <div className={styles.chat}>
      {chatHistory.length === 0 ? (
        <div className={styles.emptyChat}>
          <p>Hi! I'm Gautam's AI assistant.</p>

          <p>
            Ask me anything about his skills,
            projects, experience, or education.
          </p>
        </div>
      ) : (
        chatHistory.map((message, index) => {
          // USER MESSAGE
          if (message.role === "user") {
            return (
              <div
                className={styles.userMessage}
                key={`user-${index}`}
              >
                <p>
                  {message.content}
                </p>
              </div>
            );
          }

          // ASSISTANT MESSAGE
          if (message.role === "assistant") {
            return (
              <div
                className={styles.assistantMessage}
                key={`assistant-${index}`}
              >
                <p className={styles.assistantText}>
                    <ReactMarkdown remarkPlugins={[remarkGfm]}>
                        {message.content.text}
                    </ReactMarkdown>
                </p>

                {message.content?.links?.map((link, linkIndex) => (
                  <p
                    className={styles.link}
                    key={linkIndex}
                  >
                    <a
                      href={link}
                      target="_blank"
                      rel="noreferrer"
                    >
                      {link}
                    </a>
                  </p>
                ))}
              </div>
            );
          }
          return null;
        })
      )}

      {isLoading && (
      <div className={styles.loadingDot}>
        <span></span>
        <span></span>
        <span></span>
      </div>
)}

      <div ref={chatEndRef} />
    </div>
  );
}

export default Chat;