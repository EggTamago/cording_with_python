import React from 'react'
import './App.css'

import Header from './components/Header'
import Checkbx from './components/Checkbox'
import TimeLineChart from './components/TimeLineChart'


const App = () => {
  return (
    <div>
      <Header />
      <Checkbx />
      <TimeLineChart />
    </div>
  )
}

export default App;
