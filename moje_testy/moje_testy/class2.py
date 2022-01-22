class Order:
     def __init__(self, cart, customer):
         self.cart = list(cart)
         self.customer = customer

     def __add__(self, other):
         new_cart = self.cart.copy()
         new_cart.append(other)
         return Order(new_cart, self.customer)

order = Order(['banana', 'apple'], 'Real Python')

print((order + 'orange').cart)  # New Order instance
#['banana', 'apple', 'orange']
print(order.cart)  # Original instance unchanged
#['banana', 'apple']

order = order + 'mango'  # Changing the original instance
print(order.cart)