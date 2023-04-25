import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write( 
    """ 
    Stock Price Analyzer \n
    Shown stock prices of apple company
     """
)

ticker_symbol = "AAPL"

ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period="1d",start= "2018-01-01",end="2023-03-09")

st.write(f"""
        ### {ticker_symbol}'
        Stock Price Info:
        """)

st.dataframe(ticker_df.head())

st.write("""
        ## Daily closing prices on a Line Chart
        """)
st.line_chart(ticker_df.Close)