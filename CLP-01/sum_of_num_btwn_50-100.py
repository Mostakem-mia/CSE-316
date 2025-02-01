sum = 0;

for num in range(50,101):
    if num % 3 == 0 and num % 5 != 0:
        sum = sum + num;

print("Total Sum :", sum);