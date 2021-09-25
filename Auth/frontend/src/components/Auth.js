import React, { useContext } from 'react'
import { Redirect } from 'react-router-dom'

import { UserContext } from '../context/UserContext';

const Auth = (props) => {

    const { auth } = useContext(UserContext)
        (auth) ? props.children : <Redirect to="/login" />
}

export default Auth