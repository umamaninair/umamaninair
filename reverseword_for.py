print("What phrase do you see?")
phrase=input()
length=len(phrase)
print()
print("reversing...")
for i in range(length - 1, -1, -1):
    phrase = phrase[i]
    print(phrase[i])
print(f"The phrase in reverse order is {phrase}")




