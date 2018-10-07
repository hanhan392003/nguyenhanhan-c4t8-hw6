items = ["com", "pho", "chao", "com rang"]
print(items)

print(*items) #print tách ra, nhưng cách các chữ bằng space #separator

print(*items, sep = ", ")

#index (chỉ số)
print("Index 1")
print(items[1]) #ra pho
print("Index 0")
print(items[0])

# i = -2
# print("Index -2")

i = int(input("enter index: "))
print(items[i])
