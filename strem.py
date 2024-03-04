import yfinance as yf
import pandas as pd
import streamlit as st

st.write(

    """
# Simple Stock price app

Shown are the stock closing price and volume of Google


"""
)
tickersymbol = 'GOOGL'

tickerData = yf.Ticker(tickersymbol)

tickerDf = tickerData.history(period = '1d',start = '2010-5-31',end = '2012-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)