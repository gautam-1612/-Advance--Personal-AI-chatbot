import styles from './Header.module.css';
import useTheme from '../hooks/theme';
import { Moon, SunDim } from "lucide-react";

export default function Header() {

  const [darkMode, setDarkMode] = useTheme();

  return (
    <div className={styles.header}>
      <h2 className={styles.logo}>Ask Gautam</h2>

      <button
        onClick={() => setDarkMode((prev) => !prev)}
        className={styles.theme}
        aria-label="Toggle dark mode"
      >
        {darkMode ? (
          <SunDim size={20} />
        ) : (
          <Moon size={18} />
        )}
      </button>
    </div>
  )
}
