import logo from './logo.svg';
import './App.css';
import Button from 'react-bootstrap/Button';
import './Board';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        {/* <img src={logo} className="App-logo" alt="logo" /> */}

       Connect 4
      </header>
      <div><Board name="test"></Board></div>
    </div>
  );
}

export default App;
