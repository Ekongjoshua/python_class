"""
Imaginig you're in a charge of creating a computer system for a  computer system for a library.
This system will help keep track of who uses the library,
what books they borrow , and when they return them.

Here's how it works:
There's a list of all the people who use the library.
Think of it like a club of the library users.
There's also a list of all the books in the library.
It's like a big menu of all the books you can borrow.
If you want to take a book home, you first have to log in.
this means you tell the system your name (username).
If your name is on the list of the library members, you can log in.
If you're not on the member list , you have to sign up.
Sign up just means adding your name to the list of the library members.
Then you can log in and  borrow books. Once you're loggged in, you can choose a book you want to borrow.
When you do that, the system takes that book off the  big books list (because you're taking it)
It's like telling everyone else that you're  borrowing that book.
so, in simple terms, you're making a computer system that keeps track of who's in the library club'
which books they're  taking , and making sure only members can borrow books.
"""

"A"
# LIST FOR USERS AND BOOKS

# numbers, string: any type of data type
# key: value

members = [
    {"username": [], "borrowed_books": [],}, 
    {"username": [], "borrowed_books": [],}, 
    {"username": [], "borrowwed_books" : [],},
           ]
#           0     1    2     3      4
library = ["book1" , "book2", "book3" , "book4" , "book5"]
menu = "1. Borrow a book  2. Login  3. signup  4. logout   5. Exit"
login_status = False
current_user = None

while True:
    print(menu)
    choice = input("> ")
    
    if choice =="1":
        if login_status == True: #check that the current user/member is logged in
            user_details = members[current_user] #this indicate you most be a member to log in
            user_library = user_details['borrowed_books']
            if len(user_library) == 0:
                id = 1 #set a count for the display
                for book in library:
                    print(id , "", book) #we display the attached id along with the book name
                    
                    id = id + 1 # we increased the value of the id.
                        
                # allow the user to
                # pick a book
                selected_id = int(input("enter book id: "))
                book_index = selected_id - 1 # substract 1 from the  selected book id to get the actual index of the book
                
                
                #take out the book and add it to the borrowed list
                selected_book = library.pop(book_index)
                user_library.append(selected_book)
                print(library)
                print(user_library)
            else:
                print("exceeded borrowed limit")
                print()
                
    
        else:
            print("please login first")
    elif choice == "2":
        
        username = input("Enter username: ")
        for user in members:
            if user["username"] == username:
                login_status = True
                current_user = members.index(user)
                
                print("Login successful")
                print()

                 
    elif choice =="3":
        username = input(" choose a username: ")
     
        for user in members:
            if user['username'] == username:
                print("user already exist")
                break
        else:
            new_user = {"username" : username , "borrowed_books" : []}
            members.append(new_user)
            print("account successfully created")
            
       
    elif choice =="4":
        user_status = False
        current_user = None
        print("log out")
        print()
    
    elif choice == "5":
        break    
        
    else:
        print("invalid input")
