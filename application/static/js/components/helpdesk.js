import {React, _, autobind} from '../provider';
import Popup from "reactjs-popup";

import './helpdesk.css'


export class HelpDesk extends React.Component {
   constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

    render() {
        return <div className="helpdesk-container">
            <label>
                 Your name:
                <input className="helpdesk-input" type="text" value={this.state.value} onChange={this.handleChange}/>
            </label>
            <Popup trigger={<button className="helpdesk-btn">Book a call</button>} position="right center">
            <div dangerouslySetInnerHTML={{__html: 'We will call u ' + this.state.value}}></div>
        </Popup></div>
    }
}



