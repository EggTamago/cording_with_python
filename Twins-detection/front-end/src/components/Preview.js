import React, { useState } from "react";

const select_style = {
    margin: 20
}

const preview_style = {
    margin: 20
}

const Preview = () => {

    const [fileUrl, setFileUrl] = useState(null);

    const preview = e => {
        const imageFile = e.target.files[0];
        const imageUrl = URL.createObjectURL(imageFile);
        setFileUrl(imageUrl)
    }

    return (
        <>
            <div>
                <div style={select_style}>
                    <input type="file" onChange={preview} />
                </div>
                <div style={preview_style}>
                    <img src={fileUrl} height="300" width="300" alt="" />
                </div>
            </div>
        </>
    )
}

export default Preview;
