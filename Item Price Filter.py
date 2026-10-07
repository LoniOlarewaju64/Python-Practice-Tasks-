# This is the list of prices, it will be read by my program.
item_prices = [360.66, 50.00, 23.99, 400.00, 101.99]

# The new list is initialised so it's identified. 
expensive_items = []

# Loops are done and then prices from the list are filtered to see which is above the threshold.
for price in item_prices:
    if price > 100.00:
        expensive_items.append(price)

# The program outputs the final list.
print(expensive_items)