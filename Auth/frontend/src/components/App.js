import React, { useContext } from 'react'
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom'

import Login from "./Login"
import Home from './Home'
import UserProvider from '../context/UserContext'
import { UserContext } from '../context/UserContext'

const App = () => {

  const token = useContext(UserContext)

  return (
    <>
      <Router>
        <UserProvider>
          <Route path="/" element={<Login />} />
        </UserProvider>
      </Router>
    </>
  )
}

export default App