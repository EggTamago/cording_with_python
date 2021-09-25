import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Test from '../pages/Test'
import Test1 from '../pages/Test1'
import Test2 from '../pages/Test2'

import Logout from './Logout'
import UserInfo from './UserInfo'

const Home = () => {
    return (
        <div><h1>Hello home</h1></div>
    )
}

export default Home
