import {React, _, autobind} from '../provider';

import './account.css'

export class AccountItem extends React.Component {
    constructor(props) {
        super(props)
    }

    @autobind
    handleDeleteClick() {
        this.props.deleteAccount(this.props.account.id)
    }

    render() {

         return <tr>
            <td>{this.props.account.number}</td>
            <td>{this.props.account.balance}</td>
             <td><button className="account-item-delete-btn" onClick={this.handleDeleteClick}>delete</button></td>
        </tr>
    }
}



