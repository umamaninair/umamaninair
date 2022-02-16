print("What phrase do you see?")
phrase=input()
length=len(phrase)
print()
print("reversing...")
for i in range(length - 1, 0, -1):

    print(phrase[i],end="")
print(f"The phrase in reverse order is {phrase}")




