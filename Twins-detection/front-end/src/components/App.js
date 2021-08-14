import React from "react";

import Preview from "./Preview";

import '../css/App.css';

const App = () => {

  return (
    <div className="App">
      <header className="App-header">
        <h1>Twin or Not</h1>
        <p>upload two photos and estimate Twin or Not</p>
      </header>

      <main className="App-main">
        <Preview />
      </main>

      {/* get result from API server and indicate the result */}
      <footer>
        footer. show result
      </footer>
    </div>
  );
}

export default App;
