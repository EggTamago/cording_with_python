import React from 'react'
import { Link } from 'react-router-dom'

import Logout from '../components/Logout'
import UserInfo from '../components/UserInfo'

const Test = () => {
    return (
        <div>
            <h1>Hello this is test</h1>
            <Link to="test1"> Test1 </Link>
            <Link to="test2"> Test2 </Link>
            <Logout />
            <UserInfo />
        </div>
    )
}

export default Test