import React from 'react'
import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid';
import './App.css'

import Header from './components/Header'
import Checkbox from './components/Checkbox'
import TimeLineChart from './components/TimeLineChart'

const App = () => {
  return (
    <Box sx={{ width: '100%' }}>
      <Grid container rowSpacing={5} columnSpacing={{ xs: 1, sm: 2, md: 3 }} justifyContent="center" spacing={2}>
        <Grid item xs={12}>
          <span className="App-header"><Header /></span>
        </Grid>

        <Grid item xs={2}>
          <span className="App-checkbox"><Checkbox /></span>
        </Grid>
        <Grid item xs={9}>
          <TimeLineChart />
        </Grid>
      </Grid>
    </Box>

  )
}

export default App;

