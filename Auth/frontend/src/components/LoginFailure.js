import React, { useContext } from 'react'
import { UserContext } from '../context/UserContext'

import './App.css'

const LoginFailure = () => {

    const { count } = useContext(UserContext)

    return (
        <div className="LoginFailure">
            <h4>パスワードをもう一度入力してください<br />ログイン失敗：{count}回</h4>
        </div>
    )
}
export default LoginFailure
