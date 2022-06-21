# Menu list

list = []
print("\nYou are making a draft of menu list for your new restaurant\n")
print(" List of Menu")
print("1.List available menu")
print("2.Add a new menu")
print("3.Insert a new menu at a specified position")
print("4.Take out last menu in the list")
print("5.Remove a menu from the list")
print("6.Clear the menu")
print("E. Exit")
choice = input("choice: ")

while choice != "E" and choice != "e":
    if choice == "1":
        print("\nList available menu")
        print(list)
    elif choice == "2":
        print("\nAdd a new item")
        item = input("Input an item to add: ")
        list.append(item)
        print("Menu added")
    elif choice == "3":
        print("\nInsert a new item at a specified position")
        item = input("Input an item to add: ")
        pos = int(input("Input the index to insert: "))
        list.insert(pos,item)
        print("Menu inserted")
    elif choice == "4":
        print("\nTake out the last menu in the list")
        list.pop()
        print("Last menu has been removed")
    elif choice == "5":
        rmv = input("\nInput the name of menu to be removed: ")
        list.remove(rmv)
        print("Menu has been removed from the list")
    elif choice == "6":
        print("\nClear the menu")
        list.clear()
        print("List has been cleared")
    else:
        print("\nInvalid input")

    print("\n List of Menu")
    print("1.List available menu")
    print("2.Add a new menu")
    print("3.Insert a new menu at a specified position")
    print("4.Take out last menu in the list")
    print("5.Remove a menu from the list")
    print("6.Clear the menu")
    print("E. Exit")
    choice = input("choice: ")

if choice == "e" or choice == "E":
    print("\nExit Program")