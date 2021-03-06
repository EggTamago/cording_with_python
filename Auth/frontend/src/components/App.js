import React, { useContext } from 'react'
import { BrowserRouter as Router, Redirect, Route, Switch } from 'react-router-dom'

import { UserContext } from '../context/UserContext'

import Login from "./Login"
import Register from './Register'
import Home from './Home'
import Test from '../pages/Test'
import Test1 from '../pages/Test1'
import Test2 from '../pages/Test2'

const App = () => {

  const { auth } = useContext(UserContext)

  return (
    <Router>
      <Switch>
        <Route path="/login" component={Login} />
        <Route path="/register" component={Register} />
        {(auth) ?
          <Switch>
            <Route path="/home" component={Home} />
            <Route path="/test" component={Test} />
            <Route path="/test1" component={Test1} />
            <Route path="/test2" component={Test2} />
          </Switch>
          :
          <Redirect to="/login" />
        }
      </Switch>
    </Router>
  )
}

export default App
