member = [{"username": "pat", "borrowed": []}, {"username": "rite", "borrowed_book": []}]
library = ["book1", "book2", "book3", "book4", "book5"]
menu = "1. borrowed book 2. login 3. sign up 4. log out 5. exit"
login_status = False
current_user = None
while True:
    print(menu)
    choice = input("> ")
    if login_status == True:
        if choice == "1":
            user_details = member[current_user]
            library_user = user_details["borrowed_book"]
            if len(library_user) == 0:
                id = 1
                for book in library:
                    print(id, "", book)
                    id = id + 1
                selected_id = int(input("book_id "))
                id = id -1
                selected_book = library.pop(selected_id)
                library_user.append(selected_book)
                print(library_user)
                print(library)

            else:
                print("exceeded limit")
        else:
            print("login first")
    elif choice == "2":
        username = input("enter username: ")
        for user in member:
            if user["username"] == username:
                login_status = True
                current_user = member.index(user)
                print("login successful")
        
        
            
    elif choice == "3":
        username = input("choose a username: ")
        for user in member:
            if user["username"] == username:
                print("username already exit")
                break
        else:
            new_user = {"username": username, "borrowed_book":[]}
            member.append(new_user)
            print("account created successfully")
    elif choice == "4":
        current_user = None
        login_status = False
        print("thanks for using this app")
        
            
                
                
            
                