from slot import *
from cashRegister import CashRegister
from productInventory import ProductInventory
from exceptions import *
import threading
from datetime import time

class VendingMachine:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.slots = {}
            cls._instance.cashRegister = CashRegister()
            cls._instance.productInventory = ProductInventory()
            cls._instance.slotLock = threading.Lock()

        return cls._instance
    

    def insertMoney(self, denoms, slotID):
        if slotID not in self.slots:
            return UnknownSlot()
        
        slot = self.slots[slotID]
        if slot.state != SlotState.READY:
            raise SlotBusy()
        return slot.acceptMoney(denoms)

    def selectProduct(self, product, slotID):
        if slotID not in self.slots:
            return UnknownSlot()
        
        slot = self.slots[slotID]
        if slot.state ==  SlotState.READY:
            raise ValueError("Please Insert Cash First")
        
        elif slot.state ==  SlotState.DISPENSING:
            raise SlotBusy()
    
        productPrice  = None      
        try:
            productPrice = self.productInventory.sellProduct(product)
            change =  self.cashRegister.proceessPayment(productPrice, self.slots[slotID].insertedMoney)
        except VendingMachineError as e:
            if productPrice:  
                self.productInventory.restoreProduct(product)  # Restore inventory            
            print(f'Transaction failed due to exception: {e}')
            self.slots[slotID].insertedMoney = None
            slot.SlotState = SlotState.IDLE

        self.dispense(slotID, product, change)

        
    def dispense(self, slotID, product, change):
        if slotID not in self.slots:
            return UnknownSlot()
        
        slot = self.slots[slotID]
        slot.SlotState = SlotState.DISPENSING
        self.insertedMoney = None

        print(f'Dispensing {product} with change {change}')
        time.sleep()
        slot.SlotState = SlotState.IDLE

        
        


    
