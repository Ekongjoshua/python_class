"""
1. **Threefold Sum:** Write a program that takes three numbers as input, adds them together, and prints the sum.

2. **Number Doubler:** Create a program that takes a number as input, multiplies it by 2, and prints the result.

3. **Average Calculator:** Build a program that calculates the average of three given numbers. Take the sum of the three numbers and then divide it by 3. Print the calculated average.

4. **Circle Area Calculator:** Design a program that calculates the area of a circle. Get the radius from the user and then compute the area using the formula: area = π * radius^2.

5. **Simple Interest Calculator:** Write a program to calculate the simple interest for a given principal amount, interest rate, and time period. The formula is: simple_interest = (principal * rate * time) / 100.

6. **Temperature Converter:** Create a program that helps you convert temperatures between Celsius and Fahrenheit. Take a temperature input in one unit and provide the converted temperature.

7. **Quadratic Equation Solver:** Make a program that solves quadratic equations of the form ax^2 + bx + c = 0. Take coefficients a, b, and c as input and calculate the solutions using the quadratic formula.

8. **Rectangle Area Calculator:** Develop a program that computes the area of a rectangle. Take the length and width as input and calculate the area: area = length * width.

9. **Odd or Even:** Write a program that checks whether a given number is odd or even. Print a message accordingly.

10. **Number Swapper:** Create a program that swaps the values of two variables. Take two values as input, swap them without using a third variable, and print the swapped values.

11. **Discount Calculator:** Build a program that calculates the final price after applying a discount to an initial price. Input the initial price and discount percentage, then calculate and print the discounted price.

12. **Remainder Finder:** Design a program that calculates the remainder when one number is divided by another. Input the dividend and divisor, then print the remainder.

13. **Factorial Calculator:** Make a program that calculates the factorial of a given number. Input a number and compute its factorial: factorial = 1 * 2 * 3 * ... * n.

14. **Power Calculator:** Create a program that calculates the result of raising a number to a certain power. Input the base and exponent, then compute and print the result.

15. **Number Reverser:** Write a program that reverses the digits of a given number. Input a number, reverse its digits, and print the reversed number.

16. **Age Calculator:** Build a program that calculates your current age based on your birth year. Input your birth year, calculate your age, and print it.

17. **Triangle Area Calculator:** Develop a program that calculates the area of a triangle. Input the base and height of the triangle, then calculate and print the area: area = (base * height) / 2.

18. **Percentage Calculator:** Create a program that calculates the percentage of a number. Input the total and percentage, then calculate and print the result.

19. **Speed Calculator:** Design a program that calculates speed. Input the distance traveled and time taken, then calculate and print the speed: speed = distance / time.

20. **Leap Year Checker:** Write a program that checks if a given year is a leap year. Print a message indicating whether the year is a leap year or not.

21. **Volume Calculator:** Build a program that calculates the volume of a cube. Input the side length of the cube, then calculate and print the volume: volume = side_length^3.

22. **Equation Evaluator:** Create a program that evaluates a simple arithmetic expression containing two numbers and an operator. Input the two numbers and an operator (+, -, *, /), then calculate and print the result.

23. **Square Root Calculator:** Make a program that calculates the square root of a given number. Input a number, calculate its square root, and print the result.

24. **Time Converter:** Develop a program that converts seconds into hours, minutes, and seconds. Input the total seconds, then calculate and print the equivalent time in hours, minutes, and seconds.

25. **Rectangle Perimeter Calculator:** Write a program that calculates the perimeter of a rectangle. Input the length and width of the rectangle, then calculate and print the perimeter: perimeter = 2 * (length + width).

26. **Coin Counter:** Design a program that calculates the total value of a number of coins of different denominations. Input the number of each type of coin (pennies, nickels, dimes, quarters), then calculate and print the total value.

27. **Distance Calculator:** Create a program that calculates the distance between two points given their coordinates. Input the coordinates of two points (x1, y1) and (x2, y2), then calculate and print the distance using the distance formula.

28. **Body Mass Index (BMI) Calculator:** Build a program that calculates the Body Mass Index (BMI) given weight in kilograms and height in meters. Input weight and height, then calculate and print the BMI: BMI = weight / (height^2).

29. **Simple Calculator:** Develop a simple calculator program that performs basic arithmetic operations (+, -, *, /) on two numbers. Input two numbers and an operator, then calculate and print the result.

30. **Expression Evaluator:** Write a program that evaluates a more complex arithmetic expression containing multiple operations and parentheses. Input the expression as a string, then calculate and print the result.
"""
"""
first_number = (input("enter first number: "))
second_number = (input("enter second number:"))
third_number = (input("enter third number: "))

first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)

sum = first_number + second_number + third_number
print(sum)
"""
"""
mydict = {"name":"sam", "age": 20, "city": "boston"}
print(mydict)
value = mydict["name"]
print(value)

"""
"""
library_users = ["sam", "josh", "pet"]
book_list = ["book1" ,"book2", "book3", "book4"]

print("Welcome to my library!!")
print("Enter your details below to borrow books")
username = input("username: ")
if username in library_users:
print("logged in")
print("choose the book you want to borrow")
remove_book = input("choose a book: ")
ind = book_list.index(remove_book)
print(book_list.pop(ind))
print(book_list)
else:
print("sign up")
user = input("username: ")
if not(user in library_users):
library_users.append(user)
"""

# LISTS FOR USERS AND BOOKS
members = [{"username": "james", "borrowed_books": [],},
          {"username": "mary", "borrowed_books": [],},
          {"username": "mary", "borrowed_books": [],}
           ]

#   0   1    2    3    4 
library = ["A", "B", "C", "D", "E"]
menu = "1. Borrow a book  2. Login   3. Signup  4. Exit"
borrowed_books =[]
login_status = False
current_user = None
while True:
    print(menu)
    choice = input("> ")

    if choice == "1":
        if login_status:  #check that the current user/memeber is logged in
            user_details = members[current_user]
            user_library = user_details['borrowed_book']
            id =1 #set a count for display
            for book in library:
                print(id, "", book) #we display thebattached id along with the book name
                id = id + 1 # we increase the value of the id.

            # allow the user pick a book
            selected_id = int(input("enter book id: "))
            book_index = selected_id -1 # substract 1 from the selected book id to get the actual index of th book

            #take out the book and add it to the borrowed list
            selected_book = library.pop(book_index)
            borrowed_books.append (selected_book)

            #print the library and the borrowed_books
            print(library)
            print(user_library)
            print(borrowed_books)
        else:
            print("please login first")
    elif choice == "2":
        username = input("enter username: ")
        for user in members:
            if user["username"] == username:
                login_status = True
                current_user = members.index(user)
                print("Login successful")
                print()

    elif choice == "2":
        ...
    elif choice == "3":
        ...
    elif choice == "4":
        break
    else:
        print("invalid input")
        


