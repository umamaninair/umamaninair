print("How many numbers should I sum up")
count=int(input())
sum=0
control_variable=0
while control_variable<count:
    print(f"Please enter number {control_variable+1} of {count}:")
    number=int(input())
    sum=sum+number
    control_variable=control_variable+1
print(f"The answer is {sum}")