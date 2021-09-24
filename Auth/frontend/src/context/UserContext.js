import React, { useEffect, createContext, useState } from "react"

export const UserContext = createContext()

const UserProvider = ({ children }) => {

    const [token, setToken] = useState()
    const [auth, setAuth] = useState(false)

    useEffect(() => {
        console.log({ token })
    }, [token])

    return (
        <UserContext.Provider value={{ token, setToken, auth, setAuth }}>
            {children}
        </UserContext.Provider>
    );
}

export default UserProvider