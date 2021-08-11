import React, { Component, useState } from "react";
import { useDropzone } from 'react-dropzone';

import DropArea from "./DropArea";

import '../css/App.css';

const App = () => {

  const [images, setImages] = useState([])

  return (
    <div className="App">
      <header className="App-header">
        <h1>Twin or Not</h1>
        <p>upload two photos and estimate Twin or Not</p>
      </header>

      <main className="App-main">
        <DropArea />
      </main>
      
      {/* send 2 photos to API server */}
      <button />

      {/* get result from API server and indicate the result */}
      <footer>

      </footer>
    </div>
  );
}

export default App;
