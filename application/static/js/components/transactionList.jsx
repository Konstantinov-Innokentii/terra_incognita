import { React, _} from '../provider';
import {TransactionItem} from "./transactionItem";
import {bindActionCreators} from 'redux';
import {connect} from "react-redux";
import {fetchTransactions} from "../actions/transaction";
import {reduxForm} from "redux-form";

import './transaction-list.css'


export class TransactionsList extends React.Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="transaction-list">
                {this.props.transactions && this.props.transactions.map(transaction => <TransactionItem transaction={transaction} status={transaction.status} message={transaction.message}/>)}
            </div>
        )
    }
}

@connect(
    (state, props) => {
        return {
            transactions: state.transaction.items.sort(function (a, b) {
                return new Date(b.created) - new Date(a.created);
            }),
        }
    },
    (dispatch, props) => ({
        ...bindActionCreators({
            fetchTransactions,
        }, dispatch),
        onSubmit: (data) => dispatch(addTransaction(data))
    })
)
@reduxForm({
    form: 'account',
    enableReinitialize: true
})
export class TransactionListContainer extends React.Component {


    componentDidMount() {
        this.props.fetchTransactions({profile_id: this.props.current_user.id});
    }

    render() {
        return <TransactionsList {...this.props} />;
    }
}


