print("How many bars should be charged?")
bars_charged=int(input())
barscharged_num=0
while barscharged_num<bars_charged:
    print("Charging")
    barscharged_num=barscharged_num+1
    print(barscharged_num*"#")
print("The battery is fully charged.")