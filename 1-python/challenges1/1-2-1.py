
for attempt in range(5):
    password = input("Enter password: ")
    
    if password == "secret":
        print("access granted")
        break
    else:
        print("invalid password")
else:
    print("you are locked out")
    