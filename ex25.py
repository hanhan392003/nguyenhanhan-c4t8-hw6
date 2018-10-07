import random
words = ["left", "right", "down","high"]
word = random.choice(words)
w = list(word)
random.shuffle(w)
print ("Changed word:", "".join(w))
user_input = input("Please arrange the letters to make a right word: ")
if user_input == word:
    print("Congratulation ! You're right")
else:
    print("Sorry. This answer is false")