items = ["a","b","c"]
while True:
    
    i = input("Enter C, R, U or D: ")
    if i == "C" or i == "c":
        new_item = input("what is your hobby? ")
        items.append(new_item)
        print(items)
    elif i == "R" or i == "r":
        if len(items) != 0:
            print("this is an empty list")
        else:
            for item in items:
                print(item)
    elif i == "u" or i == "U":
        ask = input("Do you want to change anything from this list?Enter Y/N ")
        if ask == "Y" or "y":
            number = int(input("enter a number "))
            change = input("enter new item ")
            items.pop(number)
            items.append(change)
            print(items)
    elif i == "D" or i == "d":
        number = int(input("enter a number "))
        items.pop(number)
        print(items)

