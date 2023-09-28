#   0   1    2    3    4 
members = [{"name": "james", "borrowed_book": "[]"}, {"name" : "mary" , "borrowed_book" : "[]"}]
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
        



        

