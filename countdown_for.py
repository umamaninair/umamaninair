print("How far are we from the cave?")
distance=int(input())
for i in range(distance,0,-1):
    print(f"{distance} steps remaining")
    distance=distance-1
print()
print()

print("We have reached the cave!!!!")