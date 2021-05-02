import yfinance as yf

class BackTester:
    def __init__(self, ticker, start, end):
        self.start = start
        self.end = end
        self.ticker = ticker

    def __get_data(self):
        self.data = yf.download(self.ticker, start=self.start, end=self.end, progress=False)
        self.data["Return"] = (self.data["Close"] - self.data["Close"].shift(1)) / self.data["Close"].shift(1)

    def set_algo(self, algo):
        self.algo = algo

    def calc_algo_retrun(self, buySellIndi, shorting=False):
        data = self.data
        data["BuySell"] = buySellIndi
        data.dropna(inplace=True)

        if shorting:
            pass
        else:
            data["AlgoReturn"] = data["Return"]* data["BuySell"].astype(int)

        passiveReturn = (1 + data["Return"]).cumprod()[-1]
        algoReturn = (1 + data["AlgoReturn"]).cumprod()[-1]

        return {"Passive": passiveReturn,
                "Algo": algoReturn}

    def run(self):
        if self.algo == None:
            raise ValueError("No Algorithm set!")

        print("Running backtest with " + self.ticker)

        self.__get_data()
        buySellIndicator = self.algo.buySell(self.data)

        rets = self.calc_algo_retrun(buySellIndicator)

        if rets["Passive"] >= rets["Algo"]:
            print("Your algorithm on " + self.ticker + " is not performing better than a passive strategy over the defined period!")
        else:
            print(
                "Your algorithm on " + self.ticker + " performs better than a passive strategy over the defined period!")
        print(rets)

        return(rets)