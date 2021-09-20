import React from 'react'
import Button from '@material-ui/core/Button';

import axios from 'axios'

const Logout = () => {

    const handleLogout = async (e) => {
        e.preventDefault()
        const logoutAPI = 'http://127.0.0.1:4040/logout'
        await axios.delete(logoutAPI)
            .then(res => console.log(res))
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