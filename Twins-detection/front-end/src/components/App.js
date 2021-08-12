import React, { Component, useState } from "react";
import { useDropzone } from 'react-dropzone';
import { Button } from '@material-ui/core';

import DropArea from "./DropArea";

import '../css/App.css';

const App = () => {

  const [image, setImage] = useState(null)

  return (
    <div className="App">
      <header className="App-header">
        <h1>Twin or Not</h1>
        <p>upload two photos and estimate Twin or Not</p>
      </header>

      <main className="App-main">
        <DropArea />
        <DropArea />
      </main>
      
      {/* send 2 photos to API server */}
      {/* if there is no 2 photos, show error */}
      <Button variant="contained" color="secondary">
        Check Twin or Not!
      </Button>

      {/* get result from API server and indicate the result */}
      <footer>
        footer. show result
      </footer>
    </div>
  );
}

export default App;
