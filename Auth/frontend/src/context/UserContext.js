import React, { useEffect, createContext, useState } from "react"

export const UserContext = createContext()

const UserProvider = ({ children }) => {

    const [auth, setAuth] = useState(false)
    const [loginFailure, setLoginFailure] = useState(false)

    useEffect(() => {
        console.log({ auth })
    }, [auth])

    return (
        <UserContext.Provider value={{ auth, setAuth, loginFailure, setLoginFailure }}>
            {children}
        </UserContext.Provider>
    );
}

export default UserProvider