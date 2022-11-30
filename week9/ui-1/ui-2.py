import sys

def customerManager():
    while (True):
        print("------- Customer Manager -------")
        print("1. New Customer")
        print("2. All Customers")
        print("3. Search Customer")
        print("4. Edit Customer")
        print("5. Delete Customer")
        print("0. Exit")
        print("--------------------------------")
        choice2 = int(input("Enter your choice"))
        if choice2 == 1:
            print("Add new customer")
        elif choice2 == 2:
            print("All Customers")
        elif choice2 == 3:
            print("Search Customer")
        elif choice2 == 4:
            print("Edit Customer")
        elif choice2 == 5:
            print("Delete Customer")
        elif choice2 == 0:
            break
        else:
            print("Out of Range")

while(True):
    print("------- Main Menu -------")
    print("1. Customer")
    print("2. Driver")
    print("3. Trip")
    print("0. Exit")
    print("----------------------------")
    choice = int(input("Enter your choice:"))
    print("Your choice is" ,choice)
    if choice ==1:
        customerManager()
    elif choice ==2:
        print("Driver Manager")
    elif choice ==3:
        print("Trip Manager")
    elif choice ==0:
        print("BYE BYE!")
        sys.exit()
    else:
        print("Out of range")

  # if choice ==1:
    #     print("------- Customer Manager -------")
    #     choice = int(input("Enter your choice"))
    #     print("1. New Customer")
    #     print("2. All Customers")
    #     print("3. Search Customer")
    #     print("4. Edit Customer")
    #     print("5. Delete Customer")
    #     print("0. Exit")