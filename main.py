import yfinance as yf
import pandas as pd
import time
import threading

def get_stock_data(ticker_symbol):
    # Check if the stock data is in the cache
    if ticker_symbol in cache:
        # Retrieve the stock data from the cache
        stock_data_ticker = cache[ticker_symbol]
    else:
        # Try to retrieve the stock data for the ticker symbol
        try:
            stock_data_ticker = yf.Ticker(ticker_symbol).history(period="10y")
            # Store the stock data in the cache
            cache[ticker_symbol] = stock_data_ticker
        except yf.exceptions.YFinanceError as e:
            # Print an error message if the ticker symbol is invalid or the symbol has been delisted
            return

    # Remove rows with NaN values
    stock_data_ticker = stock_data_ticker.dropna()

    # Calculate the percentage change in price between the first and last rows of the DataFrame
    stock_data_ticker['pct_change'] = stock_data_ticker['Close'].pct_change()

    # Store the stock data for the ticker symbol in the dictionary
    stock_data[ticker_symbol] = stock_data_ticker

# Initialize a cache to store the stock data
cache = {}

# Use the yahoo_fin library to get a list of all NASDAQ ticker symbols
import yahoo_fin.stock_info as si
ticker_symbols = si.tickers_nasdaq()


# Initialize a dictionary to store the stock data for each ticker symbol
stock_data = {}

# Record the start time
start_time = time.perf_counter()

# Initialize a list to store the threads
threads = []

# Iterate through each ticker symbol
for ticker_symbol in ticker_symbols:
    # Create a new thread to retrieve the stock data for the ticker symbol
    thread = threading.Thread(target=get_stock_data, args=(ticker_symbol,))
    # Add the thread to the list of threads
    threads.append(thread)

# Start all the threads
for thread in threads:
    thread.start()

# Wait for all the threads to finish
for thread in threads:
    thread.join()

# Initialize a dictionary to store the highest percentage change in price for each day
highest_pct_changes_per_day = {}

# Iterate through the ticker symbols
for ticker_symbol, data in stock_data.items():
    # Group the stock data by date and find the highest percentage change in price for each day
    max_pct_changes_per_day = data.groupby(by='Date')['pct_change'].max()

    # Find the ticker symbol with the highest percentage change in price for each day
    for date, pct_change in max_pct_changes_per_day.items():
        if date not in highest_pct_changes_per_day or pct_change > highest_pct_changes_per_day[date]['pct_change']:
            highest_pct_changes_per_day[date] = {'ticker_symbol': ticker_symbol, 'pct_change': pct_change}

# Remove the oldest day from the dictionary
oldest_day = min(highest_pct_changes_per_day.keys())
del highest_pct_changes_per_day[oldest_day]

# Print the highest percentage change in price for each day
for date, data in highest_pct_changes_per_day.items():
    ticker_symbol = data['ticker_symbol']
    pct_change = data['pct_change']
    print(f"The highest percentage change in price on {date} was {pct_change:.2%} for {ticker_symbol}")

# Record the end time
end_time = time.perf_counter()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print the elapsed time
print(f"Time elapsed: {elapsed_time:.2f} seconds")
