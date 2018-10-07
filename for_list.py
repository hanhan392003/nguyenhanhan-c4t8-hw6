items = ["pho", "com", "chao"]
# print(items)
# print(*items)
# print(items[0])

# l = len(items)
# for i in range(l):
#     print(items[i])

# for item in items:
#     print(item)

for i, item in enumerate(items):
    print(i+1,".", item)