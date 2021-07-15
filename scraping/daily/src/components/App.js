import { React, useState } from 'react'
import { Button, Grid } from '@material-ui/core';
import { Wheel } from 'react-custom-roulette'

import '../css/App.css';

const App = () => {

  const data = [
    { option: '💕', style: { backgroundColor: 'green', textColor: 'black' } },
    { option: '🤩', style: { backgroundColor: 'white' } },
    { option: '💛' },
  ]

  const [mustSpin, setMustSpin] = useState(false);

  const handleSpinClick = () => {
      setMustSpin(true)
  }

  return (
    <Grid container direction="column" alignItems="center" justifyContent="center">
      <div>
        <h1>Today's choice!</h1>
      </div>

      <Wheel
      mustStartSpinning={mustSpin}
      prizeNumber={3}
      data={data}
      backgroundColors={['#3e3e3e', '#df3428']}
      textColors={['#ffffff']}

      onStopSpinning={() => {
        setMustSpin(false)
      }}
    />

    <Button onClick={() =>handleSpinClick()} variant="contained" color="primary">push me</Button>


    </Grid>
  )
}

export default App;
