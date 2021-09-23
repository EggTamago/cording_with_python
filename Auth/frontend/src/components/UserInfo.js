import React, { useContext } from 'react'
import Button from '@material-ui/core/Button';

import axios from 'axios'

import { UserContext } from '../context/UserContext'

const UserInfo = () => {

    const { token } = useContext(UserContext)

    const handleGetUserInfo = async (e) => {
        e.preventDefault()
        const userAPI = 'http://127.0.0.1:4040/user'
        await axios.get(userAPI,
            {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                }
            })
            .then(res => console.log(res))
            .catch(console.error)
    }
    return (

        <div>
            <Button variant="contained" color="primary" onClick={handleGetUserInfo}>
                userInfo
            </Button>
        </div>
    )
}

export default UserInfo