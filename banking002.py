MAIN_MENU = """
1) Register with ekon bank
2) Login
3) log out
4) Exit
"""
SUB_MENU = """
1) transfer
2) deposit
3) withdrawal
4) cancelled
"""

# users =[ 
# {"first_name": "john", "last_name": ""}
# ]
# accounts = [
#{"user_id": 0, "account_number": 1234566778}
#]

database = [{
    "user_details":{
        "first_name":"john",
        "middle_name":"elon",
        "last_name": "josh",
        "username": "google",
        "password":"john",
        "dob": "12-09-2000",
        "active": True},
    "account_details" :{
        "account_number":1234566544,
            "account_balance":2_000_000,
            "account_type":"savings", 
            "bvn":  12344554454,
            "atm_card_no": 123423, 
            "atm_card_pin":12345,},
    "transaction_details":[
        {
        "transaction_type": "deposit", 
        "sender": "elon",
        "reciever": None,
        "amount": 1_000,
        "status": "pending"
        },
        ],
    }
]
           


logged_in = False
current_user = None
#put program in an infinite loop
while True:
    print(MAIN_MENU)
    main_menu_choice = input("type here> ")
    
# check for user choice
    if main_menu_choice == "1":
        print("please enter the information below to create a new account: ")
        print("")
        name1 = input("enter first name: ")
        name2 = input("enter last name: ")
        username = input("enter username: ")
        password = input("enter password: ")
        address = input("enter addrss: ")
        account_no = int(input("enter account number: "))
        dob = input("enter date of birth: ")
        gen_bvn = int(input("enter bvn:"))
        
        
        new_user ={
        "user_details":{
        "first_name":name1,
        "last_name":name2,
        "username": username,
        "password":password,
        "dob": dob,
        "gen_bvn": gen_bvn,
        "active": True},
        
        "account_details" :{
        "account_number":1234566544,
        "account_balance":2_000_000,
        "account_type":"savings", 
        "bvn":  12344554454,
        "atm_card_no": 123423, 
        "atm_card_pin":12345,},
        "transaction_details":[]
        }
        database.append(new_user)
        print('rigistration successful')
        
                
    elif main_menu_choice == "2":
       username = input("enter username: ")
       password = input("enter password: ")
       for data in database:
           if data["user_details"]["username"] == username and data["user_details"]["password"] == password:
               current_user = database.index(data)
               logged_in = True
               print("successful")   
                                 
    elif main_menu_choice == "3":
       current_user = None
       logged_in = False
       break
    elif main_menu_choice == "4":
        print("are you sure you want to exit")
        cmd = input("N/Y ")
        if cmd.upper() == "Y":
            print("thanks for banking with us")
            break
            
    else:
        print("invalid choice:", main_menu_choice)  
    print("")
    
        
    while True:
        print(SUB_MENU)
        SUB_MENU_choice =input("> ")
        if SUB_MENU_choice == "1": 
            reciever_details = input("enter recievers username: ")
            sent_amount = float(input("amount: "))
            new_trans = {"transaction_type": "transfer", 
                        "sender": "me", 
                        "reciever": reciever_details,
                        "amount": sent_amount, 
                        "status":"pending,"
                        }
            current_user = ["transaction_details"].append(new_trans)
            print("transaction pending")
            
        elif SUB_MENU_choice == "2":
            depo_details = input("enter your username; ")
            depo_amount =  int(input("enter amount"))
            new_trans=    {
        "transaction_type": "deposit", 
        "sender": depo_details,
        "reciever": [],
        "amount": depo_amount,
        "status": "successful"
        },
            current_user = database.append(new_trans)  
            print(depo_amount, "deposited successful") 
              
        elif SUB_MENU_choice =="3":
            wit_amount = int(input("enter amount: "))
            new_trans = {"transaction_type": "withdrawal", 
            "sender": None,
            "reciever": "me",
            "amount": wit_amount,
            "status": "succesful"}
            current_user = database.append(new_trans)
            print(wit_amount, "withdraw successful")

    

        elif SUB_MENU_choice == "4":
            break

        
