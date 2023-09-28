"""
Conditions/conditional statements are a way we tell the computer what to do depending on the outcome of something.
Example:
 1. The phone screen brightness usually get brighter in bright-light(When you are outdoors and it's really sunny)
 2. When a face doesn't match what the phone recognises the phone doesn't unlock.

These conditions/conditional statement make the computer seem smart and know what to do.
     
     a > b:
if <condition>:
....<code we want to execute>
....<code we want to execute>
....<code we want to execute>
....<code we want to execute>
<code here>


the thing with the if-statement is that;
  1. You must start with the 'if' keyword
  2. you must have your condition(this usually determines the outcome of the code(True or False after evaluating))
  3. you must add the colon ':' immediately after the condition.
  4. any code/instruction that should be implemented if the condition results to a True should be indented
  using a single tab or four spaces as represented by the (....) four dots above
  5. anything that is not to do with the conditon you are trying to work with should not be added into the
  indentation.
"""

"""
Conditions
This is usually a comparison made between two values that result to True or False and if
the result is True the code that was indented would be executed.

What do we use for this comparison:
a = 10
b = 20
>     ;  a > b  ;  False
<     ;  a < b  ;  True
>=    ;  a >= b ;  False
<=    ;  a <= b ;  True
==    ;  a == b ;  False

logical operators:
and
or
not

a = 10
b = 20
c = 10
d = 20

if any of the conditions is False the entire evaluation becomes false
a < b and c < d  ;  True
a > b and c < d    ;  False

a < b or c < d    ;  True
a > b or c < d    ;  True


not(a > b)  ; True
not(a < b)  ; False
"""

# A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.
"""
COST = 100
quantity = int(input("How many items are you buying: "))
total_cost = COST * quantity
if total_cost > 1000:
    print("You are getting 10% discount")
    discount = total_cost * (10 / 100)
    total_cost = total_cost - discount
    print("After your discount, total cost is:", total_cost)
else:
    print("Your total cost is:", total_cost)
    """
import time
cost = 100
purchase_items = int(input("quantity of items:" ))
purchase_cost = purchase_items * cost
discount_cost = purchase_cost * (10/100)
payment = purchase_cost - discount_cost
if purchase_cost > 1000:
  print("you're on a discounted sales")
  time.sleep(4)
  print("total",payment)