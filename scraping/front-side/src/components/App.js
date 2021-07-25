import { React, useState } from 'react'
import { Button, Grid } from '@material-ui/core';

import axios from 'axios'

import '../css/App.css';

const App = () => {

  const [name, setName] = useState('')

  const server = 'http://localhost:4040/';
  const fastapi = () => {
      console.log('start http communicate')
      axios.get(server)
        .then(res => setName(res.data[0]))
        .catch(console.error)
  }

  return (
    <Grid container direction="column" alignItems="center" justifyContent="center">
      <div>
        <h1>Today's choice!</h1>
      </div>

    <Button onClick={() =>fastapi()} variant="contained" color="primary">push me</Button>

    <p>Today is ...  {name} </p>

    </Grid>
  )
}

export default App;
