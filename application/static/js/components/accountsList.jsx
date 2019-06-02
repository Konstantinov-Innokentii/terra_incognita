import { React, _} from '../provider';
import { connect } from 'react-redux'

import {AccountItem} from "./accountItem";
import {addAccount, deleteAccount, fetchAccounts} from "../actions/account";
import {fetchTransactions} from "../actions/transaction";

import {bindActionCreators} from "redux";

import './accountList.css'

class AccountList extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className='account-list-container'>
                <table>
                    <thead>
                    <tr>
                        <td>Number</td>
                        <td>Balance</td>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.accounts && this.props.accounts.map(account => <AccountItem account={account}
                                                                                            deleteAccount={this.props.deleteAccount}
                                                                                            key={account.id}/>)}
                    </tbody>
                </table>
                <button className="account-add-btn" onClick={this.props.addAccount}>Add</button>
            </div>
        )
    }
}

@connect(
    (state, props) => {
        return {
            accounts: state.account.items.sort(function (a, b) {
                return new Date(b.created) - new Date(a.created);
            }),
            transactions: state.transaction.items,
        }
    },
    (dispatch, props) => {
        return {
            ...bindActionCreators({
                fetchAccounts,
                addAccount,
                fetchTransactions
            }, dispatch),
            deleteAccount: (id) => dispatch(deleteAccount(id))
        }
    }
)
export class AccountListContainer extends React.Component{

    componentDidMount(){
       this.renewData()
    }

    renewData(){
        this.props.fetchAccounts({profile_id: this.props.current_user.id});
        this.props.fetchTransactions({profile_id: this.props.current_user.id})
    }

    render (){
        return <AccountList {...this.props} renewData={this.renewData}/>
    }
}

