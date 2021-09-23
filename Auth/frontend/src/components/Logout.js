import React, { useContext } from 'react'
import Button from '@material-ui/core/Button';

import axios from 'axios'

import { UserContext } from '../context/UserContext'

const Logout = () => {

    const { token, setToken } = useContext(UserContext)



    const handleLogout = async (e) => {
        e.preventDefault()
        const logoutAPI = 'http://127.0.0.1:4040/logout'
        console.log(token)

        await axios.delete(logoutAPI,
            {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                }
            })
            .then(res => setToken(null))
            .catch(console.error)
    }
    return (

        <div>
            <Button variant="contained" color="primary" onClick={handleLogout}>
                Logout
            </Button>
        </div>
    )
}

export default Logout