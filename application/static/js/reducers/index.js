import { combineReducers} from "redux"
import { accountReducer } from "./account";
import { userReducer} from "./user";
import {transactionReducer} from "./transaction";
import { reducer as formReducer } from 'redux-form'


export const rootReducer = combineReducers({
    account: accountReducer,
    current_user: userReducer,
    transaction: transactionReducer,
    form: formReducer,
});