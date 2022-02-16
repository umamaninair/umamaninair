print("How many cables I must avoid")
cables_avoid=int(input())
live_cables=0
while live_cables<cables_avoid:
    print("Avoiding")
    live_cables=live_cables+1
    print(f"...Done! {live_cables} live cable avoided!")
print("All live cables have been avoided.")