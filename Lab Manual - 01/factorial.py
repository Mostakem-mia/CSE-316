number = int(input("Enter any positive integer number: "));

factorial = 1;

if number == 0 or number == 1:
    print(f"The factorial of {number} is 1");

else:
    for num in range(1,number+1):
        factorial = num * factorial;
        
print(f"The factorial of {number} is :", factorial);
