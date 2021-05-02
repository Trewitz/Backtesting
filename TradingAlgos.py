class BuySellAlgo:
    def __init__(self):
        raise NotImplementedError

    def buySell(self):
        raise NotImplementedError


class SimpleMA(BuySellAlgo):
    def __init__(self, lowerMA, upperMA):
        self.lowerMA = lowerMA
        self.upperMA = upperMA

    def buySell(self, data, type="Close"):
        lowerMA = data[type].rolling(self.lowerMA).mean()
        upperMA = data[type].rolling(self.upperMA).mean()

        upperMA.dropna(inplace=True)
        lowerMA = lowerMA.loc[upperMA.index]
        return lowerMA > upperMA

class BollingBands(BuySellAlgo):
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def buySell(self, data, type="Close"):
        bolu = data[type].rolling(self.n).mean() + self.m * data[type].rolling(self.n).std()
        bold = data[type].rolling(self.n).mean() - self.m * data[type].rolling(self.n).std()

        # Price should be between upper and lower band
        output = data[type] < bold
        return output
