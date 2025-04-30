from typing import Dict
from exceptions import *

class ProductInventory:
    def __init__(self, products: Dict[str, int]):
        self.products = products
    
    def addProducts(self, products):
        for item, attr in products.items():
            price, count = attr
            if item in self.products:
                self.products = [price, count]
            else:
                self.products[item][0] = price
                self.products[item][1] = count


    def restockProduct(self, item, count):
        if item in self.products:
            self.products[item][1] += count
        else:
            raise UnknownProductError()
        
    def sellProduct(self, productId):
        if productId in self.products and self.products[productId][1] > 0:
           self.products[productId][0] -= 1
           return self.products[productId][1]
        else:
            raise OutofStockError()
             



        

    