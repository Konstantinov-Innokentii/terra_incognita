const initialState = {
    items: [],
    isFetching: false,
};

export function transactionReducer(state = initialState, action) {
    switch (action.type) {
        case 'REQUEST_TRANSACTION':
            return {
                ...state,
                isFetching: true
            };

        case 'RECEIVE_TRANSACTION':
            return {
                ...state,
                isFetching: false,
                items: [...action.transactions],
            };


        case 'ADD_TRANSACTION_SUCCESS':
            return {
                ...state,
                items: [...state.items, action.transaction]
            };


        default:
            return state
    }
}

