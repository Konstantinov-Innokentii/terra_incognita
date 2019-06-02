import 'babel-polyfill';

import {React, ReactDOM, _, $} from './provider';
import { createStore} from 'redux'
import { Provider, connect } from 'react-redux'
import {Switch, Route, BrowserRouter, Link} from 'react-router-dom'

import {rootReducer} from "./reducers";
import {loadAuthenticatedProfile} from "./actions/user";
import {AccountListContainer} from "./components/accountsList";
import thunk from "redux-thunk";
import { applyMiddleware} from "redux";
import { composeWithDevTools } from 'redux-devtools-extension';

import {TransactionFormContainer} from "./components/transactionForm";
import {TransactionListContainer} from "./components/transactionList";


import './styles.css'
import {HelpDesk} from "./components/helpdesk";

@connect(
    (state, props) => {
        return {
            current_user: state.current_user
        }
    },
    (dispatch, props) => {
        return {
            loadAuthenticatedProfile : () => dispatch(loadAuthenticatedProfile()),
        }
    }
)

class TerraApp extends React.Component {

    constructor(props) {
        super(props);
    }

    componentDidMount(){
        this.props.loadAuthenticatedProfile();
    }

    render() {
        return (
            <React.Fragment>


                {this.props.current_user.id && <BrowserRouter>
                     <header>
                         <div className="link-block">
                         <Link to="/terra"> Main </Link>
                         <Link to="/transaction"> Transaction </Link>
                         <Link to="/history"> History </Link>
                         <Link to="/helpdesk"> Helpdesk </Link>
                          <a href="/auth/signout" title="exit">
                                   <div>Exit</div>
                          </a>
                         </div>
                </header>
                     <div id="content">
                    <Switch>
                        <Route path="/terra"
                               render={(props) => <AccountListContainer current_user={this.props.current_user}/>}/>
                        <Route path="/transaction"
                               render={(props) => <TransactionFormContainer current_user={this.props.current_user}/>}/>
                        <Route path="/history"
                               render={(props) => <TransactionListContainer current_user={this.props.current_user}/>}/>
                          <Route path="/helpdesk"
                               render={(props) => <HelpDesk/>}/>

                    </Switch>
                         </div>
                </BrowserRouter>}

            </React.Fragment>
        )
    }
}


$(function () {
    const appEl = document.getElementById('app');

    let store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)));
    ReactDOM.render(
        <Provider store={store}>
            <TerraApp/>
        </Provider>,
        appEl
    );
});
