import React,{Component} from 'react';
import Button from 'react-bootstrap/Button';
import 'bootstrap/dist/css/bootstrap.min.css';

export class Navbar extends Component {

    render() {
        return(
            <div className="nav">
                <h1>Connect 4</h1>

                <h3>2 Players. Red and Yellow. Who do you think will win?</h3>

                {/* <input type="text" placeholder="Enter your bets here..."></input> */}
                <div className="buttonRow">
                <Button variant="danger" className="btn-primary">Red</Button>{' '}
                <Button variant="warning" className="btn-primary" >Yellow</Button>{' '}
                <Button variant="light" >Tie</Button>{' '}
            </div>
            </div>
        )
    }
}