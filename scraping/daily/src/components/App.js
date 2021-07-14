import React from 'react'
import { Button, Grid } from '@material-ui/core';

import '../css/App.css';

const App = () => {

  const who = () => {
    console.log("click this button")
  }

  return (
    <Grid container alignItems="center" justifyContent="center">
      <div>
        <h1>Today's choice!</h1>
      </div>

      <Button onClick={() => who()} variant="contained" color="primary">push me</Button>

    </Grid>
  )
}

export default App;
