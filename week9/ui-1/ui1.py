import sys

while(True):
    print("------- Main Menu -------")
    print("1. Insert Driver")
    print("2. Display All Drivers")
    print("3. Search Driver")
    print("4. Edit Driver")
    print("5. Delete Driver")
    print("0. Exit")
    print("---------------------------")
    choice = int(input("Enter your choice"))
    print("---------------------------")
    if choice == 0:
        print("Bye!")
        sys.exit() #program exit
    elif choice >= 6 or choice <0:
        print("Choice out of range")
    elif choice ==1:
        print("Insert Driver")
    elif choice ==2:
        print("Display All Drivers")
    elif choice ==3:
        print("Search Driver")
    elif choice ==4:
        print("Edit Driver")
    elif choice ==5:
        print("Delete Driver")