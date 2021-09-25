import React, { useContext } from 'react'
import { Redirect } from 'react-router-dom'

import Users from './Users'

const Auth = (props) => (

    Users.isLoggedIn ? props.children : <Redirect to="/login" />

)

export default Auth