members = [{"username": "john", "borrowed_book": []},{"username": "pat","borrowed_book": []}]
library = ["book1", "book2", "book3"]
menu = " 1. borrowed book 2. login 3. sign up 4. log out 5. exit "
current_user = None
login_statue = False
while True:
    print(menu)
    choice = input(">> ")
    
    if choice == "1":
        if login_statue == True:
            user_details = members[current_user]
            library_user = user_details["borrowed_book"]
            if len(library_user) == 0:
                id = 1
                for books in library:
                    print(id ,"", books)
                    
                    id = id + 1
                select_id = int(input("book id: "))
                book_id = select_id - 1
                
                selected_book = library.pop(book_id)
                library_user.append(selected_book)
                print(library)
                print(library_user)
            else:
                print("exceeded limit")
        else:
            print("login to borrowed book")
    elif choice == "2":
        username = input("enter username: ")
        for user in members:
            if user["username"] == username:
                login_statue = True
                current_user = members.index(user)
                print('Login successful')
    elif choice == "3":
        username = input("choose a username: ")
        for user in members:
            if user["username"] == username:
                print("username already taken")
                break
        else:
            new_user = {"username":username, "borrowed_book": []}
            print("account created successfully")
    elif choice == "4":
        current_user = None
        login_statue = False
        print("thanks for using our library")
    elif choice == "5":
        cmd = input("N/Y ")
        if cmd == 'Y':
            print("thanks for your usage")
        else:
            break
            
        
                


        
        
    
            
        
        
    
    


    


    