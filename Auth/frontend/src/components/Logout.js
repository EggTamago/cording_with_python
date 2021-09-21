import React, { useContext } from 'react'
import Button from '@material-ui/core/Button';

import axios from 'axios'

import { UserContext } from '../context/UserContext'

const Logout = () => {

    const { setToken } = useContext(UserContext)

    const handleLogout = async (e) => {
        e.preventDefault()
        const logoutAPI = 'http://127.0.0.1:4040/logout'
        await axios.delete(logoutAPI)
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