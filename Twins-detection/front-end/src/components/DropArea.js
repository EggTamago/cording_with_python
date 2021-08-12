import React, { Component, useCallback, useState } from "react";
import { useDropzone } from 'react-dropzone'

const style = {
  width: 300,
  height: 300,
  border: "1px dotted #888",
  margin: 20,
  transition: 'border .5s ease-in-out'
}

const DropArea = () => {

  const onDrop = useCallback(acceptedFiles => {
    // save the image to send API server
    // need using FileReader API and preview images
    console.log('acceptedFiles:', acceptedFiles)
  }, [])
  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop })

  return (
    <>
      <div {...getRootProps()} style={style}>
        <input {...getInputProps()} />
        {
          isDragActive ? <p>drop!</p> : <p>drop image</p>
        }
      </div>
    </>
  )
}

export default DropArea;
