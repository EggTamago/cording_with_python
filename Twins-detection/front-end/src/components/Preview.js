import React, { useState } from "react"

import axios from 'axios'

const style = {
    margin: 20
}

const Preview = () => {

    // fileUrl is for preview image
    const [fileUrl, setFileUrl] = useState(null)
    // image is for send API server
    const [imageList, setImageList] = useState(null)
    // response is for get response from API server
    const [response, setResponse] = useState(null)

    const preview = (e) => {
        const imageFile = e.target.files[0]
        setImageList(e.target.files)
        console.log(e.target.files.length)
        const imageUrl = URL.createObjectURL(imageFile)
        setFileUrl(imageUrl)
    }

    const server = 'http://127.0.0.1:4040/upload'

    const submit = (e) => {
        e.preventDefault()
        const formData = new FormData()
        formData.append("image", imageList[0])
        axios.post(server, formData, { headers: { 'Content-Type': 'multipart/form-data' } })
            .then(res => setResponse(res.data))
            .catch(console.error)
    }

    return (
        <>
            <form>
                <div style={style}>
                    <input type="file" name="image" onChange={preview} multiple />
                    <input type="submit" value="submit" onClick={submit} />
                </div>
                <div style={style}>
                    <img src={fileUrl} height="300" width="300" alt="" />
                </div>
            </form>
        </>
    )
}

export default Preview;
