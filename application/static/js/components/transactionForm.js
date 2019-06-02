import React, {Component} from 'react'
import { Field, reduxForm } from 'redux-form'
import {bindActionCreators} from 'redux';
import {addTransaction} from "../actions/transaction";
import {fetchAccounts} from "../actions/account";

import { connect } from 'react-redux'


import Select from 'react-select';

import './transaction-form.css'

class RenderSelectInput extends Component {

    render()
    {
        return (
            <Select
                {...this.props}
                value={this.props.input.value}
                onChange={(value) => this.props.input.onChange(value)}
                onBlur={() => this.props.input.onBlur(this.props.input.value)}
                options={this.props.options}
                placeholder={this.props.placeholder}
            />
        );
    }
}


const TransactionForm = ({handleSubmit, onSubmit, ...props}) => {
    return (
        <form className='form-transaction' onSubmit={handleSubmit(onSubmit)}>
            <div className='form-field'>
                <label htmlFor="target">Target</label>
                <Field name="target" component="input" type="text"/>
            </div>
            <div className='form-field'>
                <label htmlFor="source">Source</label>
                <Field name="source" component={RenderSelectInput} options={props.accountOptions}/>
            </div>
            <div className='form-field'>
                <label htmlFor="value">Value</label>
                <Field name="value" component="input"/>
            </div>
            <div className='form-field'>
                <label htmlFor="message">Message</label>
                <Field name="message" component="input"/>
            </div>
            <button className="form-transaction-btn" type="submit">Submit</button>
        </form>
    )
};


@connect(
    (state, props) => {
        let accountOptions = state.account.items.map(account => ({label: `account: ${account.number}  balance: ${account.balance}`, value: account.number}));

        return {
            accountOptions: accountOptions,
        }
    },
    (dispatch, props) => ({
        ...bindActionCreators({
            fetchAccounts,
        }, dispatch),
        onSubmit: (data) => dispatch(addTransaction(data))
    })
)
@reduxForm({
    form: 'account',
    enableReinitialize: true
})
export class TransactionFormContainer extends React.Component {


    componentDidMount() {
        this.props.fetchAccounts({profile_id: this.props.current_user.id});
    }

    render() {
        return <TransactionForm {...this.props} />;
    }
}
