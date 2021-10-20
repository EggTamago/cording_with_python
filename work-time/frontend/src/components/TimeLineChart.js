import React from 'react'

import { ComposedChart, Line, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const sampleData = [
    {
        name: '1',
        day: 8,
        month: 8,
    },
    {
        name: '2',
        day: 10,
        month: 18,
    },
    {
        name: '3',
        day: 10,
        month: 28,
    },
    {
        name: '4',
        day: 0,
        month: 28,
    },
    {
        name: '5',
        day: 11,
        month: 39,
    },
    {
        name: '6',
        day: 12,
        month: 250,
    },
    {
        name: '7',
        day: 12,
        month: 250,
    }, {
        name: '1',
        day: 8,
        month: 8,
    },
    {
        name: '2',
        day: 10,
        month: 18,
    },
    {
        name: '3',
        day: 10,
        month: 28,
    },
    {
        name: '4',
        day: 0,
        month: 28,
    },
    {
        name: '5',
        day: 11,
        month: 39,
    },
    {
        name: '6',
        day: 12,
        month: 250,
    },
    {
        name: '7',
        day: 12,
        month: 250,
    }, {
        name: '1',
        day: 8,
        month: 8,
    },
    {
        name: '2',
        day: 10,
        month: 18,
    },
    {
        name: '3',
        day: 10,
        month: 28,
    },
    {
        name: '4',
        day: 0,
        month: 28,
    },
    {
        name: '5',
        day: 11,
        month: 39,
    },
    {
        name: '6',
        day: 12,
        month: 250,
    },
    {
        name: '7',
        day: 12,
        month: 250,
    }, {
        name: '1',
        day: 8,
        month: 8,
    },
    {
        name: '2',
        day: 10,
        month: 18,
    },
    {
        name: '3',
        day: 10,
        month: 28,
    },
    {
        name: '4',
        day: 0,
        month: 28,
    },
    {
        name: '5',
        day: 11,
        month: 39,
    },
    {
        name: '6',
        day: 12,
        month: 250,
    },
    {
        name: '7',
        day: 12,
        month: 250,
    }, {
        name: '1',
        day: 8,
        month: 8,
    },
    {
        name: '2',
        day: 10,
        month: 18,
    },
    {
        name: '3',
        day: 10,
        month: 28,
    },
    {
        name: '4',
        day: 0,
        month: 28,
    },
    {
        name: '5',
        day: 11,
        month: 39,
    },
    {
        name: '6',
        day: 12,
        month: 250,
    },
    {
        name: '7',
        day: 12,
        month: 250,
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
            <YAxis yAxisId={1} label={{ value: "day", angle: -90, dx: -20 }} ticks={[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]} />
            <YAxis
                yAxisId={2}
                orientation="right"
                domain={[0, 5]}
                ticks={[0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]}
                label={{ value: "month", angle: -90, dx: 20 }}
            />
            <Tooltip />
            <Legend />
            <Bar yAxisId={1} dataKey="day" barSize={20} fill="#413ea0" />
            <Line yAxisId={2} type="monotone" dataKey="month" stroke="#ff7300" />
        </ComposedChart>
    )
}

export default TimeLineChart
