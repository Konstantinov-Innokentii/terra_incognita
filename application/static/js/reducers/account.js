const initialState = {
    items: [],
    isFetching: false,
};

export function accountReducer(state = initialState, action) {
    switch (action.type) {
        case 'REQUEST_ACCOUNT':
            return {
                ...state,
                isFetching: true
            };

        case 'RECEIVE_ACCOUNT':
            return {
                ...state,
                isFetching: false,
                items: [...action.accounts],
            };


        case 'DELETE_ACCOUNT_SUCCESS':
            return {
                ...state,
                items: state.items.filter(account =>
                    account.id !== action.id
                )
            };

        case 'ADD_ACCOUNT_SUCCESS':
            return {
                ...state,
                items: [...state.items, action.account]
            };


        default:
            return state
    }
}

