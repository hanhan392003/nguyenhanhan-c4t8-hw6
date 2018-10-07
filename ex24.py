n = input("input a word: ")
print("Jumble word :")
for i in range(len(list(n))-1,-1, -1):
    print(list(n)[i].upper())
