import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get date on this ticker
tickerData = yf.Ticker(tickerSymbol)
# get histricla data(Open, Close, High, Low...)
tickerDF = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.write("""
# Close price
""")
st.line_chart(tickerDF.Close)

st.write("""
# Volume
""")
st.line_chart(tickerDF.Volume)
