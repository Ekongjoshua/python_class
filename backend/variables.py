"""
Programming is basically telling the computer what to do and how to do it.


Variables:
Are containers for storing values in our programs.
For every variable that we define and assign a value to, the computer create a location in it's memory to be able to store that value.

The type of data we assign to the variable allows the computer know how much space it needs to create to store that value.

the location of the variable could be like this "1bxcrxv1jg" which is quite
difficult to memorize or understand, hence the use of variable.
"""
"""
x = 10
y = 1100
z = x * y
print(z)


working_hours = 10
wage_per_hour = 1100
pay = working_hours * wage_per_hour
print(pay)
"""
"""
input("promt"):
This is an in-built function in python that allows us to collect or take information from our users through the command line interface(CLI).

the "prompt" is a message that should be displayed on the command line to enable the user know what information they are to enter.

by default, all values accepted through this function is a string. to get numeric or other types of value from the user, you would have to convert the default value to
the desires type of value.

This conversion process is called Casting
"""
# Example: write a program to display the product of two numbers
first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

# Casing
first_number = int(first_number)
second_number = int(second_number)

# calculate the product
product = first_number * second_number
print(product)


"""
Mnemonic variable naming convention.
1. Name your variable in a way that you can remember
2. Name them to be descriptive enough to tell the kind of value they are holding
3. No use of spaces or embedded characters when naming a variable
4. If a variable consists of multiple words, use an underscore('_') to relace the spaces.
5. Do not begin your variable name with numbers or any other characters but numbers can be added at the end of the variable name.
"""