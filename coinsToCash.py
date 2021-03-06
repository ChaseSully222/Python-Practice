# Create a function that will take all your coins and convert it to the cash amount.

# def calc_dollars(**coins):
    # The function should look at each key (pennies, nickels, dimes and quarters) and perform the appropriate math on the integer value to determine how much money you have in dollars. Store that value in a variable named `dollarAmount` and print it.

# calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)

def calc_dollars(**coins):

  total = 0

  for coin, amount in coins.items():
    if coin == "pennies":
      total += amount * 0.01
    if coin == "nickels":
      total += amount * 0.05
    if coin == "dimes":
      total += amount * 0.10
    if coin == "quarters":
      total += amount * 0.25
  print("Total =", total)

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
# The output would be 8.07 when the function is executed with those arguments.
