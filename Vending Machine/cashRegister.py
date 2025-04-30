from exceptions import InsufficientFunds, InsufficientChangeError
from threading import Lock

class CashRegister:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.register = {}
            cls.Lock = Lock()
        return cls._instance
    
   

    def addToRegister(self, denoms):
        for denom, count in denoms:
            if denom in self.register:
                self.register[denom] += count
            else:
                self.register[denom] =  count
        self.register = {k: self.register[k] for k in sorted(self.register, reverse=True)}

    def processPayment(self, productPrice, insertedCash):
        totalCash =  sum(insertedCash.values())
        if totalCash < productPrice:
            raise InsufficientFunds()
        
        ret = {}
        with self.Lock:
            change = totalCash - productPrice
            self.addToRegister(insertedCash)

            for denom, count in self.register.items():
                if denom > change:
                    continue

                changeCount = change // denom
                if changeCount >= count:
                    change -= changeCount * denom
                    ret[denom] = changeCount
                    self.register[denom] -= changeCount
                else:
                    change -= self.register[denom] * denom
                    ret[denom] = self.register[denom]
                    self.register[denom] = 0

                if change == 0:
                    return ret
            self.rejectPayment(insertedCash)
            raise InsufficientChangeError()
        
    def rejectPayment(self, insertedCash):
        for denom, count in insertedCash:
                self.register[denom] -= count

        





    