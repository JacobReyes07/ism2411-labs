# --- DISCLOSURE ---
# I did use Claude to interpret the errors from exercise 5 into plain english.
# I found the AI to be a helpful tool because it could look at an error that I had never seen anything like
# before, then tell me what it meant which then helped me to see the code from a different perspective that I had missed which put me
# in a better position to fix it then.

# Self Assessment 1
# The first error I noticed was the missing colon. When I read the error what stuck out to me was the word SYNTAX and the arrow pointed
# at the place where it was missing. From this information I was able to piece together what went wrong myself without the help of AI and
# then just add it in.

# Self Assessment 2
# apply_discount(price, tier) Checks which tier matches by filtering from the top down. Whenever the tier matches the filter it
# takes the price, and adds a multiplier to apply the discount.

# Exercise 1 Defining a function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $200 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05)}")

# Exercise 2

def apply_discount(price, tier):
    if tier == 'gold':
        return price * 0.85
    elif tier == 'silver':
        return price * 0.9
    elif tier == 'bronze':
        return price * 0.95
    else:
        return price

# Calling the function with different tiers
original_price = 200

for tier in ['gold', 'silver', 'bronze', 'none']:
    print (f"{tier}: ${apply_discount(original_price, tier):.2f}")
    
# Exercise 3

def final_price(price, rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.09

for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 5

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# The first error is on line 10. It gave me an error that said,
# File "c:\Users\reyes\OneDrive\Documents\ism2411\unit1\module07\broken_sales.py", line 10
#                   ^
# SyntaxError: expected ':'
# PS C:\Users\reyes\AppData\Local\Programs\Microsoft VS Code>
# This means that on line 10 it needs the colon which basically means "then".

# The second error is on line 16. It gave me an error that said,
# Traceback (most recent call last):
#  File "c:\Users\reyes\OneDrive\Documents\ism2411\unit1\module07\broken_sales.py", line 16, in <module>
#    print(sales[i])
#          ~~~~~^^^
# IndexError: list index out of range
# The problem that is happening here is that it tries to print(sales[i]) and add 1 to i all the way until i is greater than the
# length of sales which is only 5 long. Because i starts at 0 and the way python counts the first thing in a list as 0 and the second as 1
# and so on, it means that the first thing it does when it is told to print(sales[0]) is it prints the first integer in the list. Next when
# it does 1 it prints the second. This continues until it gets to 4 which prints the last integer of the list and adds one to i to make it 5.
# But because 5 is still equal to the length of the list which is 5, it causes it to try to print(sales[5]). Because there is no 6th integer
# in the sales list it gives the error that the list index is out of range. I can fix this by replacing the <= sign with just a < sign.

# Exercise 6

x = 100

def double_it(x):
    x = 200
    return x * 2

print(x) # prints 100 because it is not part of the double_it function so it just reads that the value of x is 100 without seeing the part within the double_it function that says otherwise..
print(double_it(x)) # prints 400 because in the definition of what the double it function does it changes the value of x to 200 and then returns double it.
print(x) # still prints 100 because it still doesn't look at the x within the double_it function because it is not using that function.