import sys
list1 = []
print("---Main Menu ---")
print("1. Add")
print("2. Display All")
print("0. Exit")
print("------------------------")
choice = int(input("Enter your choice : "))
print("------------------------")
print("Your choice is : {}".format(choice))
if (choice>=0 and choice<=2):
    match choice:
        case 1:
            tmp = int(input("Enter any number : "))
            list1.append(tmp)
        case 2:
            print(list1)
        case 0:
            print("Bye!")
            sys.exit()