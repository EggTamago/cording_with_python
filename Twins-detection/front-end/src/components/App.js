import React, { Component, useState } from "react";
import { useDropzone } from 'react-dropzone';

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

        <div>
          <p>upload image 1</p>
        </div>

        <div>
          <p>upload image 2</p>
        </div>
      
      </main>

      <footer>

      </footer>
    </div>
  );
}

export default App;
