def check_login():
    flag = False
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    for i in range(3):
        confirm_password = input("Re-enter Password: ")
        if password == confirm_password:
            flag = True
            break
    if flag == True:
        print(f"Login success. Welcome {username}")
    else:
        print("Maximum attempts reached. Please try again!")

check_login()