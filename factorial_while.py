print("Please enter a number:")
number=int(input())
control_variable=1
factorial=1
while control_variable<number+1:
    factorial=factorial*control_variable
    control_variable=control_variable+1
print(f"The factorial is {factorial}")
