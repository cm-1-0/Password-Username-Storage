print("Welcome to the vault")
prompt = input("Would you like to access this program?: ")
while prompt == "Yes":
    text = input("Would you like to access your account: ")
    if text == "Yes":
        password = input("Welcome, what is the password for this program?: ")
        if password == "abcd":
            a = 1
            print("Evaluating password")
            while a < 4:
                print(str(a) + "...")
                a += 1
            print("Access Granted")
            who_user = input("Pick an user: ")


            def keys():
                print(user_details[str(input("Enter a username or password to access: "))])


            if who_user == "Colin":
                master_pass = input("Type the master password for this user: ")
                if master_pass == "0colin4":
                    username1 = input("Enter a username or email to store: ")
                    password1 = input("Enter a password to store: ")
                    access = input("Would you like to access a username or password? ")
                    user_details = {"username1": username1,
                                    "password1": password1,
                                    }
                    if access == "Yes":
                        keys()
                else:
                    print("Fail, Restart program ")
            else:
                print("Try again")
        else:
            print("Try again")
    else:
        print("Thank You and come again")
    break
if prompt == "No":
    print("Thank You and come again")

