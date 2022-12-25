# Stock Data Processor

Welcome to the Stock Data Processor! This Python script allows you to retrieve and analyze stock data for all NASDAQ ticker symbols with just a few simple commands.

Using the yfinance library, the script retrieves the stock data for each ticker symbol and calculates the percentage change in price between the first and last rows of the data. It also groups the stock data by date and finds the highest percentage change in price for each day, so you can easily identify the top performing stocks on a daily basis.

To improve performance, the script uses multi-threading to retrieve the stock data in parallel and caches the data to reduce API calls.

Here are some examples of the output you can expect from the script:

| Date       | Ticker Symbol | Percentage Change in Price |
|------------|---------------|----------------------------|
| 2022-01-01 | AAPL          | 10.00%                     |
| 2022-01-02 | GOOGL         | 5.00%                      |
| 2022-01-03 | MSFT          | 3.00%                      |
| 2022-01-04 | AMZN          | 7.50%                      |
| 2022-01-05 | FB            | 4.50%                      |


## Features
- Retrieve and analyze stock data for all NASDAQ ticker symbols.
- Calculate the percentage change in price between the first and last rows of the data for each ticker symbol.
- Group the stock data by date and find the highest percentage change in price for each day.
- Use multi-threading to retrieve the stock data in parallel, which can significantly improve performance.
- Cache the stock data to improve performance and reduce API calls.

## Requirements
- Python 3.6 or later
- yfinance library

## Usage
To run the script, execute the following command in the terminal:

```
python main.py
```

The script will retrieve the stock data for all NASDAQ ticker symbols, calculate the percentage change in price for each ticker symbol, and print the highest percentage change in price for each day.

## Notes
The stock data is cached to improve performance and reduce API calls.
The script uses multi-threading to retrieve the stock data in parallel, which can significantly speed up the process.

## License
This project is licensed under the MIT License. 
