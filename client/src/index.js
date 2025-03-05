import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import ReactDOM from 'react-dom';
import {createRoot} from 'react-dom/client';
import Navbar from './components/Navbar';

import{
    BrowserRouter as Router, 
    Switch, 
    Route
} from 'react-router-dom'
import HomePage from './components/Home';
import LoginPage from './components/Login';
import CreateSolaresPage from './components/CreateSolares';

const App=()=>{
    return (
        <Router>
            <div className="container">
                <Navbar/>
                <Switch>
                    <Route path='/crear_solares'>
                        <CreateSolaresPage/>
                    </Route>  
                    <Route path='/login'>
                        <LoginPage/>
                    </Route>
                    <Route path='/'>
                        <HomePage/>
                    </Route>
                </Switch>
            </div>
        </Router>
    )
}
const root = createRoot(document.getElementById('root'));
root.render(<App/>);