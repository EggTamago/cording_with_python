import React, { useContext } from 'react'
import { BrowserRouter as Router, Redirect, Route, RouteProps, Switch } from 'react-router-dom'

import { UserContext } from '../context/UserContext'

import Auth from './Auth'
import Login from "./Login"
import Home from './Home'
import Test from '../pages/Test'
import Test1 from '../pages/Test1'
import Test2 from '../pages/Test2'



const App = () => {

  return (

    <Router>
      <Switch>
        <Route path="/login" component={Login} />
        <Auth>
          <Switch>
            <Route exact path="home" component={Home} />
            <Route exact path="test" component={Test} />
            <Route exact path="test1" component={Test1} />
            <Route exact path="test2" component={Test2} />
          </Switch>
        </Auth>
      </Switch>
    </Router>

  )
}

export default App
