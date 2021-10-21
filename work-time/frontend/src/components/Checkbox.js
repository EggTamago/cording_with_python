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

    const handleSubmit = async (e) => {
        e.preventDefault()

        const server = 'http://127.0.0.1:4040/'
        await axios.get(server)
            .then(res => console.log(res))
            .catch(console.error)
    }

    return (
        <form>
            <table >
                <tbody>
                    {checkBoxList.map((key, index) =>
                        <tr key={index}>
                            <th><input type="radio" name="radio" /></th>
                            <td><label>{key}</label></td>
                        </tr>
                    )}
                </tbody>
            </table>
            <input type="submit" value="Submit" onClick={handleSubmit} />
        </form>
    )
}

export default Checkbox
