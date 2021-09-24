import React, { useContext } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Login from "./Login"
import Home from './Home'
import { UserContext } from '../context/UserContext'

const App = () => {

  const adminUser = {
    username: "test",
    password: "test"
  }

  const { auth } = useContext(UserContext)

  return (
    <>
      {(auth) ? (
        <Home />
      ) : (
        <Login />
      )}


      {/* {        <Switch>
          <Route exact path='/' component={Login} />
          <Route path='/home' component={Home} />
        </Switch>} */}
    </>
  )
}

export default App