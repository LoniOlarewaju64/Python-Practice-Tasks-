#This is a prompt for the user. They must type in dollar amount.
print("Welcome! You are using a currency converter. 1 USD is equal to 0.92 EUR")

usd_amount = float(input("Enter the amount in USD: "))

# Conversion rate is a decimal number. 
exchange_rate = 0.92

# The inputted number and the exchange rate are multiplied to output a number
eur_amount = usd_amount * exchange_rate

# Print the result
print(f"{usd_amount} USD is equal to {eur_amount:.3f} EUR")