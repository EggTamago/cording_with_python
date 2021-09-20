import React from 'react'
import { BrowserRouter as Router, Switch, Route, Redirect } from 'react-router-dom'

import Login from "./Login"
import Logout from './Logout'
import UserProvider from '../context/UserContext'

const App = () => {
  return (
    <>
      <UserProvider>
        <Login />
      </UserProvider>
    </>
  )
}

export default App