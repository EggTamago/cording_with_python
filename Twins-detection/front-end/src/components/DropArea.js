import React, { useCallback, useState } from "react";
import { useDropzone } from 'react-dropzone'


const style = {
  width: 300,
  height: 300,
  border: "1px dotted #888",
  margin: 20,
  transition: 'border .5s ease-in-out'
}

const DropArea = () => {

  const [srcUrl, setSrcUrl] = useState(null)

  // using FileReader API and preview images
  const onDrop = useCallback(acceptedFiles => {

    acceptedFiles.forEach((file) => {
      const reader = new FileReader()

      reader.onabort = () => console.log('file reading was aborted')
      reader.onerror = () => console.log('file reading has failed')
      reader.onload = (e) => {

        
      }
      reader.readAsArrayBuffer(file)
    })
  }, [])

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop })

  return (
    <>
      <div {...getRootProps()} style={style}>
        <input {...getInputProps()} />
        { isDragActive ? <p>drop!!!</p> : <p>put image here</p> }
        { console.log(srcUrl)}
      </div>
      
    </>
  )
}

export default DropArea;
