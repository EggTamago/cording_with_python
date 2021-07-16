import { React, useState } from 'react'
import { Button, Grid } from '@material-ui/core';

import axios from 'axios'


import '../css/App.css';

const App = () => {

  const server = 'http://localhost:8000/';
  const fastapi = (e) => {
      console.log('start http communicate')
      axios.get(server)
        .then((res) => { console.log(res); })
        .catch(console.error);
  }

  return (
    <Grid container direction="column" alignItems="center" justifyContent="center">
      <div>
        <h1>Today's choice!</h1>
      </div>

    <Button onClick={() =>fastapi()} variant="contained" color="primary">push me</Button>


    </Grid>
  )
}

export default App;
