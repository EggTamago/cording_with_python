import React, { useState } from "react"

import axios from 'axios'

const style = {
    margin: 20
}

const Preview = () => {

    // fileUrl is for preview image
    const [fileUrl, setFileUrl] = useState(null)
    const [image, setImage] = useState(null)

    const preview = e => {
        const imageFile = e.target.files[0]
        setImage(imageFile)
        const imageUrl = URL.createObjectURL(imageFile)
        setFileUrl(imageUrl)
    }

    const server = 'http://127.0.0.1:4040/upload'

    const submit = (e) => {
        e.preventDefault()
        const formData = new FormData()
        formData.append("image", image)
        axios.post(server, formData, { headers: { 'Content-Type': 'multipart/form-data' } })
            .then(res => console.log(res))
            .catch(console.error)
    }

    return (
        <>
            <form>
                <label>
                    <div style={style}>
                        <input type="file" name="file" onChange={preview} />
                        <input type="submit" value="submit" onClick={submit} />
                    </div>
                </label>
                <div style={style}>
                    <img src={fileUrl} height="300" width="300" alt="" />
                </div>
            </form>
        </>
    )
}

export default Preview;
