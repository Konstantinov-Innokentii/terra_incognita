import axios from 'axios'

export const addAccount = () => {
  return dispatch => {
    axios
      .post(`/api/v1/account`)
      .then(res => {
        dispatch(addAccountSuccess(res.data));
      })
  };
};

const addAccountSuccess = account => ({
  type: 'ADD_ACCOUNT_SUCCESS',
  account: account
});


export const deleteAccount = (id) => {
    return  dispatch => {
       axios.delete(`/api/v1/account/${id}`)
           .then(res => {
               dispatch(DeleteAccountSuccess(id));
           })
    }
};

const DeleteAccountSuccess = id => ({
    type: 'DELETE_ACCOUNT_SUCCESS',
    id: id
});

export function fetchAccounts(params) {
    return dispatch => {
        dispatch(requestAccount());
        (axios.get(`/api/v1/account`, {params: params}))
            .then(response => dispatch(receiveAccount(response.data)));
    }
}
const requestAccount = () => ({
  type: 'REQUEST_ACCOUNT'
});


const receiveAccount = (data) => ({
    type: 'RECEIVE_ACCOUNT',
    accounts: data,
});


