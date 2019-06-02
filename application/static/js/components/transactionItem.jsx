import {React, _, autobind} from '../provider';

import './transaction-item.css'


export class TransactionItem extends React.Component {
    constructor(props) {
        super(props)
    }


    render() {
        return <div className={this.props.transaction.status ? "transaction-success" : "transaction-fail"}>
            <div className="transaction-field">Value:  {this.props.transaction.value}</div>
            <div className="transaction-field">Source:  {this.props.transaction.source}</div>
            <div className="transaction-field">Target:  {this.props.transaction.target}</div>
            <div className="transaction-field">
                <div className="message-title">Message: </div>
            <div className="message" dangerouslySetInnerHTML={{__html: this.props.transaction.message}}></div>
            </div>
        </div>
    }
}

