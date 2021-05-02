import numpy as np
from BackTester import BackTester
from TradingAlgos import SimpleMA, BollingBands

## Packages for downloading financial data
from pytickersymbols import PyTickerSymbols

if __name__ == '__main__':
    np.random.seed(1)
    stock_data = PyTickerSymbols()
    german_stocks = stock_data.get_stocks_by_index('DAX')
    german_stocks = [*german_stocks]

    stockSymbols = {}
    for stock in german_stocks:
        symbols = stock["symbols"][0]
        stockSymbols[stock["name"]] = symbols["yahoo"]


    for symbol in stockSymbols.keys():
        backtester = BackTester(stockSymbols[symbol], start='2015-04-23', end='2021-04-23')
        #maAlgo = SimpleMA(50, 200)
        bbAlgo = BollingBands(20, 2)
        backtester.set_algo(bbAlgo)
        backtester.run()






