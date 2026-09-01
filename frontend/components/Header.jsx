import { useSelector, useDispatch } from 'react-redux';
import { toggleTheme } from '../slice/theme';
import styles from './Header.module.css';

export default function Header() {

  const theme = useSelector((state) => state.theme.theme);
  const dispatch = useDispatch();

  return (
    <div className={styles.header}>
      <h2 className={styles.logo}>Ask Gautam</h2>

      <button
        className={styles.theme}
        onClick={() => dispatch(toggleTheme())}
      >
        {theme === "light" ? "☀️" : "🌙"}
      </button>
    </div>
  )
}
