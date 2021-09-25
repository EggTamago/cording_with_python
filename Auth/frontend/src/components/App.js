import React, { useContext } from 'react'

import Login from "./Login"
import Home from './Home'
import { UserContext } from '../context/UserContext'

const App = () => {

  const { auth } = useContext(UserContext)

  return (
    <>
      {(auth) ? (
        <Home />
      ) : (
        <Login />
      )}
    </>
  )
}

export default App