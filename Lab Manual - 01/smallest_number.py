number = [5,4,3,4,2,1,9,8,7];

smallest = number[0];

for num in number:
    if num < smallest:
        smallest = num;
    
print("Smallest Number is ",smallest);