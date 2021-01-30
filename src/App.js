import './App.css';
import {Navbar} from './components/Navbar';
 

import Button from 'react-bootstrap/Button';
// import Board from './Board';
import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import Game from './Game';

function App() {
  return (
    <div className="App">
       <header className="App-header">

    <div className="Container">
    <Navbar />
    </div>
    </header>

      <div className="board"><Game ></Game></div>
    </div>
    
  );
}

export default App;
