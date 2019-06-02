const initialState = {};

export function userReducer(state = initialState, action) {
    switch (action.type) {
        case 'FETCH_AUTHENTICATED_PROFILE':
            return {...state, ...window.user};
        default:
            return state
  }
}
