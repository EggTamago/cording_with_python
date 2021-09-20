import React, { useEffect, createContext, useState } from "react"

export const UserContext = createContext()

const UserProvider = ({ children }) => {

    const [token, setToken] = useState(null)

    useEffect(() => {
        console.log({ token })
    }, [token])

    return (
        <UserContext.Provider value={{ token, setToken }}>
            {children}
        </UserContext.Provider>
    );
}

export default UserProvider