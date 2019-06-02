import axios from 'axios'
import { push } from 'react-router-dom';


export const addTransaction = (data) => {
    console.log(data);
    return dispatch => {
        axios
            .post(`/api/v1/transaction`, {...data, 'source': data.source.value})
            .then(res => {
                dispatch(addTransactionSuccess(res.data));
            }).then( () => {
            window.location.replace('/history');
        })
    };
};

const addTransactionSuccess = transaction => ({
  type: 'ADD_TRANSACTION_SUCCESS',
  transaction: transaction
});

export function fetchTransactions(params) {
    return dispatch => {
        dispatch(requestTransaction());
        (axios.get(`/api/v1/transaction`, {params: params}))
            .then(response => dispatch(receiveTransaction(response.data)));
    }
}
const requestTransaction = () => ({
  type: 'REQUEST_TRANSACTION'
});


const receiveTransaction = (data) => ({
    type: 'RECEIVE_TRANSACTION',
    transactions: data,
});

