import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'

import Test from '../pages/Test'
import Test1 from '../pages/Test1'
import Test2 from '../pages/Test2'

import Logout from './Logout'
import UserInfo from './UserInfo'

const Home = () => {
    return (
        <>
            <Switch>
                <Route exact path='/' component={Test} />
                <Route exact path='/test1' component={Test1} />
                <Route exact path='/test2' component={Test2} />
            </Switch>
        </>
    )
}

export default Home
