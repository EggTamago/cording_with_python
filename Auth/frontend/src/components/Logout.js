import React, { useContext } from 'react'
import { Link } from 'react-router-dom';
import Button from '@material-ui/core/Button';

import axios from 'axios'

import { UserContext } from '../context/UserContext'

const Logout = () => {

    const { setAuth } = useContext(UserContext)

    const handleLogout = async (e) => {
        e.preventDefault()
        const logoutAPI = 'http://127.0.0.1:4040/logout'
        await axios.delete(logoutAPI,
            {
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(res => setAuth(false))
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