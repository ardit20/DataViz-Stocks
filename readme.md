## Tech Stocks Intereactive Data Viz App

This Python code visualizes the adjusted close prices of several popular tech stocks including Apple (AAPL), Amazon (AMZN), Google (GOOGL) etc.

Using the **yfinance** library, it downloads historical stock prices for the selected tickers from 2015 to 2023. Then, using **Streamlit** and **Plotly**, the code creates an interactive line plot that shows the adjusted close prices for each selected stock.

With a date slider and a dropdown menu, the user can easily select the desired date range and the specific stocks they want to analyze. The plot is interactive, and you can hover over any point on the lines to see the exact date and corresponding price.

This code tracks the performance of several popular tech stocks and can help investors make informed decisions about their portfolio. With its clean and visually appealing plot, this code provides an easy and accessible way to analyze stock prices.

## Libraries Used 

**yfinance**: to download historical market data from Yahoo! Finance.

**pandas**: for data manipulation and cleaning

**plotly**: for the interactive data vizualization 

**streamlit**: to build interactive web app


**mplcursors**: a library that adds interactive data cursors to matplotlib plots, allowing the user to click on a plot point and view the corresponding data value.
