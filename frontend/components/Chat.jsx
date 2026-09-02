import styles from './Chat.module.css'
import { useSelector } from 'react-redux';


function Chat() {

  const chatHistory = useSelector((state) => state.chatHistory.chatHistory);

  return (<>
    {chatHistory.length === 0 ? (<div className={styles.emptyChat}>
            <p>Hi! I'm Gautam's AI assistant.</p>
            <p>Ask me anything about his skills, projects, experience, or education.</p>
        </div>) : (
            chatHistory.map((message) => {
                if(message.role === 'user') {
                    return (
                        <div className={styles.userMessage} key={message.content}>
                            <p>{message.content}</p>
                        </div>
                    )
                }
                if(message.role === 'assistant') {
                    return (
                        <div className={styles.assistantMessage} key={message.content}>
                            <p>{message.content}</p>
                            {message.links && message.links.map(link => <p key={link.name}>{link.name} <a href={link.url} target="_blank" rel="noreferrer">{link.url}</a></p>) }
                        </div>
                    )
                }
            })
        )
    }
  </> 
  )
}

export default Chat;
