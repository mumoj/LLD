class VendingMachineError(Exception): pass

class UnknownProductError(VendingMachineError): pass

class OutofStockError(VendingMachineError): pass

class InsufficientChangeError(VendingMachineError): pass

class InsufficientFunds(VendingMachineError): pass

class SlotBusy(VendingMachineError): pass

class UnknownSlot(VendingMachineError): pass