import React, { useState, useEffect } from "react"
import '../css/Checkbox.css'

const Checkbox = () => {

    // list of checkbox
    const checkBoxList = [
        'Keiichiro Tani',
        'Taro Tanaka',
        'Hanako Ito'
    ]

    const [check, setCheck] = useState()
    useEffect(() => {
        // get data from db when check is changed
        console.log('get data')
    }, [check])

    return (
        <div>
            {checkBoxList.map((key) =>
                <table>
                    <tr>
                        <th><input id="check" type="checkbox" name="name" /></th>
                        <td><label htmlFor="check">{key}</label></td>
                    </tr>
                </table>
            )}
        </div>
    )
}

export default Checkbox
