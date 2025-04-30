The vending machine should support multiple products with different prices and quantities - ProductInventory.
The machine should accept coins and notes of different denominations - CashInventory.
The machine should dispense the selected product and return change if necessary -
The machine should keep track of the available products and their quantities - 

The machine should handle multiple transactions concurrently and ensure data consistency.

The machine should provide an interface for restocking products and collecting money.

The machine should handle exceptional scenarios, such as insufficient funds or out-of-stock products. - Exceptions

VendingMachine.
- Insert Money
    - calculate Amount from denominations.
    - start timer - if unable to select with 5 Mins - dispense cash back.

- Select Product -> 
    - keyMappings to diffrent products.
    - check if product is available()
    - if not raise OutOfStockException

    - If amount not enough for product:
        raise InsufficientFunds()

    if amount more than enough:
    - dispense change

   
ProductDispenser:
    - dispense product


InventoryManager
 - addProduct
 - restockProduct
 

CashRegister
-AddCash
-Collect Cash


Transaction:
    - currentCash
    - TransactionExpiryTime
        while datetime.now() < transactionExpiryTime and product not selected:
            printf('Please select an item')
    - if productSeleted:
        - check currentCash > product.price:
          change = currentCash - product.price
    getChange(change: float) -> Map[str, int]:
          



          



 







