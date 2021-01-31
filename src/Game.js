import React, {Component} from 'react';
import ReactDOM from 'react-dom';

var coord = [[0,0],[1,0],[0,3],[0,5],[3,2],[2,4],[1,1],[2,2]]
var board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],]

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
  
  async function timeout(delay) {
    return new Promise( res => setTimeout(res, delay) );
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
         timeout(1000);
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
  