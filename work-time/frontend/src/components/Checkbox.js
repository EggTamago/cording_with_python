import React, { useState, useEffect } from "react"
import '../css/Checkbox.css'

import axios from 'axios'

const Checkbox = () => {

    // list of checkbox
    const checkBoxList = [
        'ABC DEF',
        'Taro Tanaka',
        'Hanako Ito'
    ]

    const [check, setCheck] = useState("")
    useEffect(() => {
        // get data from db when check is changed
        console.log('get data')
    }, [check])

    const handleCheckBox = async (e) => {
        const server = 'http://127.0.0.1:4040/'
        await axios.get(server)
            .then(res => console.log(res))
            .catch(console.error)
    }

    return (
        <div>
            {checkBoxList.map((key, index) =>
                <table key={index}>
                    <tbody>
                        <tr>
                            <th><input type="checkbox" onChange={handleCheckBox} value={key} /></th>
                            <td><label>{key}</label></td>
                        </tr>
                    </tbody>
                </table>
            )}
        </div>
    )
}

export default Checkbox
