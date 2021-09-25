import React, { createContext, useState } from "react"

export const UserContext = createContext()

const UserProvider = ({ children }) => {

    const [auth, setAuth] = useState(false)
    const [loginFailure, setLoginFailure] = useState(false)
    const [count, setCount] = useState(0)

    return (
        <UserContext.Provider value={{ auth, setAuth, loginFailure, setLoginFailure, count, setCount }}>
            {children}
        </UserContext.Provider>
    );
}

export default UserProvider