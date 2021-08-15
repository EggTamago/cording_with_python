import React, { useState } from "react"

import axios from 'axios'

import 'bootstrap/dist/css/bootstrap.min.css'
import '../css/App.css'

const style = {
    margin: 20
}

const Preview = () => {

    const [fileUrl, setFileUrl] = useState([])  // fileUrl is for preview image
    const [imageList, setImageList] = useState(null)  // image is for send API server
    const [response, setResponse] = useState(0)  // response is for get response from API server

    const preview = (e) => {
        // setImageList is for send data to API server
        setImageList(e.target.files)
        // following is for preview
        for (let i = 0; i < e.target.files.length; i++) {
            const imageFile = e.target.files[i]
            const imageUrl = URL.createObjectURL(imageFile)
            setFileUrl(fileUrl => [...fileUrl, imageUrl])
        }
    }

    const submit = async (e) => {
        e.preventDefault()
        const server = 'http://127.0.0.1:4040/upload'
        const formData = new FormData()
        for (let i = 0; i < imageList.length; i++) {
            formData.append(i, imageList[i])
        }
        await axios.post(server, formData, { headers: { 'Content-Type': 'multipart/form-data' } })
            .then(res => setResponse(res.data))
            .catch(console.error)
    }

    return (
        <div>
            <form>
                <div style={style}>
                    <input class="form-control" type="file" name="image" onChange={preview} multiple="multiple" />
                </div>

                <div>
                    <img src={fileUrl[0]} height="300" width="400" alt="" />
                    <img src={fileUrl[1]} height="300" width="400" alt="" />
                </div>

                <div>
                    <input type="submit" value="submit" class="btn mb-3 mt-3 btn-lg btn-block btn-outline-light" onClick={submit} />
                </div>
            </form>

            {/* get result from API server and indicate the result */}
            <footer style={style}>
                <p> Twin score : {response} %</p>
            </footer>
        </div>
    )
}

export default Preview;
