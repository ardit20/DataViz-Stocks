import yfinance as yf
import streamlit as st
import pandas as pd
import plotly.express as px

# Define a list of ticker symbols for tech stocks
tickers = ['AAPL', 'MSFT', 'AMZN', 'GOOGL', 'TSLA', 'NVDA', 'PYPL', 'NFLX', 'CRM', 'ADBE', 'INTC', 'CSCO', 'IBM', 'TXN', 'QCOM', 'AVGO', 'AMD', 'MU']

# Download historical stock prices for the tickers using yfinance
tech_stocks = yf.download(tickers, start='2015-01-01', end='2023-03-03')

# Create a date slider to select the date range
start_date = st.date_input('Start date', value=pd.to_datetime('2015-01-01'), min_value=pd.to_datetime('2015-01-01'), max_value=pd.to_datetime('2023-03-03'))
end_date = st.date_input('End date', value=pd.to_datetime('2023-03-03'), min_value=start_date, max_value=pd.to_datetime('2023-03-03'))

# Filter the tech_stocks DataFrame to include only the selected date range
selected_tech_stocks = tech_stocks.loc[start_date:end_date]

# Create a dropdown menu to select the stocks
selected_tickers = st.multiselect('Select your stocks', tickers)

# Filter the selected_tech_stocks DataFrame to include only the selected tickers
selected_stocks = selected_tech_stocks['Adj Close'][selected_tickers]

# Reshape the DataFrame for Plotly
selected_stocks = selected_stocks.reset_index().melt(id_vars='Date', var_name='Ticker', value_name='Price')

# Create an interactive line plot with tooltips using Plotly
fig = px.line(selected_stocks, x='Date', y='Price', color='Ticker', hover_data=['Price'])
fig.update_layout(
    title='Adjusted Close Prices Over Time',
    xaxis_title='Date',
    yaxis_title='Price ($)',
    hovermode='x unified',
    hoverlabel=dict(font_size=14)
)

# Show plot
st.plotly_chart(fig)