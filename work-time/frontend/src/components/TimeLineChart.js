import React from 'react'

import { ComposedChart, Line, Area, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const sampleData = [
    {
        name: '1',
        day: 8,
        sum: 8,
    },
    {
        name: '2',
        day: 10,
        sum: 18,
    },
    {
        name: '3',
        day: 10,
        sum: 28,
    },
    {
        name: '4',
        day: 0,
        sum: 28,
    },
    {
        name: '5',
        day: 11,
        sum: 39,
    },
    {
        name: '6',
        day: 12,
        sum: 250,
    },
]

const TimeLineChart = () => {

    return (
        <ComposedChart
            width={1500}
            height={800}
            data={sampleData}
            margin={{
                top: 5,
                right: 30,
                left: 20,
                bottom: 5,
            }}
        >
            <CartesianGrid stroke="#f5f5f5" />
            <XAxis dataKey="name" padding={{ right: 50, left: 50 }} />
            <YAxis yAxisId={1} label={{ value: "hours/day", angle: -90, dx: -20 }} />
            <YAxis
                yAxisId={2}
                orientation="right"
                domain={[0, 5]}
                tickCount={6}
                label={{ value: "sum", angle: -90, dx: 20 }}
            />
            <Tooltip />
            <Legend />
            <Bar yAxisId={1} dataKey="day" barSize={20} fill="#413ea0" />
            <Line yAxisId={2} type="monotone" dataKey="sum" stroke="#ff7300" />
        </ComposedChart>
    )
}

export default TimeLineChart
