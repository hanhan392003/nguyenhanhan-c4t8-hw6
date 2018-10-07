# ex 1
emptylist = []
print(emptylist)

# ex 2
list1 = ["sport"]
print(list1)

# ex 3
list2 = ["sport", "books", "robots"]
print(list2)

# ex 4
list2.append("computers")
print(list2)

# ex 5
new_items = input("enter a hobby: ")
list2.append(new_items)
print(list2)

# ex6
print(*list2)

# ex 7
print(*list2, sep = ", ")

# ex 8
print(*list2, sep = "|")

# ex 9
print(list2[0])
print(list2[-1])
print(list2[-2])

# ex 10
print(list2[0].upper())
print(list2[-1].upper())
print(list2[-2].upper())

# ex 11
list2.pop(0)
list2.append("Spider Man")
print(list2)

# ex 12
list2.pop(-1)
list2.append("Dragon Ball")
print(list2)

# ex 13
i = int(input("Enter the index: "))
list2.pop(i)
list2.append(input("enter something: "))
print(list2)

# ex 14
list2.pop(2)
print(list2)

# ex 15
for i in list2:
    if i == "LOL":
        list2.remove(i)
if "LOL" not in list2:
    print("Check the items in the list again")

# ex 16
i = int(input("Enter the index of the item you want to delete: "))
list2.pop(i)
print(list2)

# ex 17
i = input("Enter the item you want to delete: ")
list2.remove(i)
print(list2)

# ex 18
for i in ["sleep", "eat", "code"]:
    list2.append(i)
for item in list2:
    print(item)

# ex 19
for item in list2:
    print(item.upper())

# ex 20
for i, item in enumerate(list2):
    print(i+1, ".", item.upper())

# ex 21
for item in list2:
    if "e" in list(item) or "E" in list(item):
        print(item.upper())