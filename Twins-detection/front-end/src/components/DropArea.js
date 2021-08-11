import React, { Component, useState } from "react";
import { DropzoneArea } from 'material-ui-dropzone';


const DropArea = () => {
    return (
      <>
          <div className="App-dropzone">
            <p>upload image 1</p>
            <DropzoneArea
              acceptedFiles={['image/*']}
              dropzoneText={"Drag and drop an image here or click"}
              onChange={(files) => console.log('Files:', files)}
            />
          </div>
  
          <div className="App-dropzone">
            <p>upload image 2</p>
            <DropzoneArea
              acceptedFiles={['image/*']}
              dropzoneText={"Drag and drop an image here or click"}
              onChange={(files) => console.log('Files:', files)}
            />
          </div>

      </>
    );
  }
  
  export default DropArea;
  