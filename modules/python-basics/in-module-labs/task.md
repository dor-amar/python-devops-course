## **Shopping Cart Total Calculator**

**The goal:**

- Multiply each product’s price by the quantity
- Add them all together
- Return the total price

```python
def calculate_cart_total(cart_items, product_prices):
    """
    Calculates the total price of all items in the cart.
    `cart_items` is a dictionary with product names as keys and quantities as values.
    `product_prices` is a dictionary with product names and price per unit.
    """

# Example product prices
product_prices = {
    "apple": 3.0,
    "banana": 2.5,
    "milk": 7.0,
    "bread": 5.0
}

# Example cart items (product: quantity)
cart_items = {
    "apple": 2,
    "milk": 1,
    "bread": 3
}

total = calculate_cart_total(cart_items, product_prices)
print(total)  # Expected: 2*3.0 + 1*7.0 + 3*5.0 = 6 + 7 + 15 = 28.0

"""
To complete this exercise:
---------------------------

1. Create the `calculate_cart_total()` function.
2. Use a loop to go over each item in the cart.
3. Multiply quantity by the unit price from `product_prices`.
4. Return the total value.

Bonus ideas:
------------
- Make the cart interactive: ask the user to input items one by one in a loop.
- Handle products not found in the price list.
- Allow the user to type 'done' to finish the cart.
- Display a summary of what the user ordered with a final total.
"""
```