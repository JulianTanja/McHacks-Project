import React, {Component} from 'react';
import ReactDOM from 'react-dom';

var coord = [[5,6],[5,5],[5,4],[5,3],[5,2],[5,1],[4,3],[4,1]]
var board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]


const axios = require('axios');
axios.get('/test')
.then(function (response){
  console.log(response)
})
class Square extends React.Component {
  constructor(props){
    super(props);  
    // this.props = {
    //   backgroundColor: 
    // }
    var color = "white";
    if(this.props.backgroundColor == 1){
      color = "red";
    }
    if(this.props.backgroundColor == 2){
      color = "yellow";
    }
    this.state={
      show: false,
      backColor: color
    }
  }


 
    render() {
      return (
        <button className="square" style={{
            backgroundColor: this.state.backColor     
        }}>
        {this.props.value}
      </button>
      );
    }
  }
  
 

  class Board extends React.Component {
     render() {
      var b = false;
      const chng = coord.map(it => {
        if(b){
          board[it[0]][it[1]] = 1
          b = !b
        }else{
          board[it[0]][it[1]] = 2
          b= !b
        }
      })
      const boardup = board.map(item => (
          item.map(ite => (
          <Square backgroundColor={ite}></Square>
        ))
        
      ))
      return boardup;
    }
  }

  
  class Game extends React.Component {
    render() {
      return (
          <div className="game-board">
            <Board />
          </div>

      );
    }
  } 
  export default Game;
  
  // ========================================
  
//   ReactDOM.render(
//     <Game />,
//     document.getElementById('root')
//   );
  