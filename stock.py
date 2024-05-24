class Stock:
    def _init_(self, ticker: str, price: int, volume: int):
        self.ticker = ticker
        self.price = price
        self.volume = volume

    def getSymbol(self) -> str:
        return self.ticker
    
    def getPrice(self) -> int:
        return self.price 
    
    def getVolume(self) -> int:
        return self.volume
    
    def display(self):
        print("Symbol: ", self.ticker, ", Price: ", self.price, ", Volume: ", self.volume)