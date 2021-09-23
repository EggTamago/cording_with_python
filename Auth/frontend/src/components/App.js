import React, { useContext } from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Login from "./Login"
import Home from './Home'
import UserProvider from '../context/UserContext'
import { UserContext } from '../context/UserContext'

const App = () => {

  const adminUser = {
    username: "test",
    password: "test"
  }


  const { token } = useContext(UserContext)

  return (
    <>
      {(token == null) ? (
        <Login />
      ) : (
        <Home />
      )}


      {/* {        <Switch>
          <Route exact path='/' component={Login} />
          <Route path='/home' component={Home} />
        </Switch>} */}
    </>
  )
}

export default App