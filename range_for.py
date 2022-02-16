print("What level of brightness is required?")
level=int(input())
print()
print("Adjusting brightness...")
for i in range(2,level+2,2):
    print("Beep's brightness level:"+("*"*i))
    print("Bop's brightness level:"+("*"*i))
print()
print("Adjustments complete!")
