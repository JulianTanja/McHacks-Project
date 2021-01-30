import React,{Component} from 'react';
import Button from 'react-bootstrap/Button';

export class Navbar extends Component {

    render() {
        return(
            <div className="nav">
                <h1>Connect 4</h1>

                <h3>2 Players. Red and Yellow. Who would you like to win?</h3>

                <input type="text" placeholder="Enter your bets here..."></input>

                <Button variant="light">Enter</Button>

            </div>
        )
    }
}