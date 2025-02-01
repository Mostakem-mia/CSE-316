number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];

sum_of_odd = 0;
sum_of_even = 0;

for n in number:
    if n%2==0:
        sum_of_even = sum_of_even+n;
    else:
        sum_of_odd = sum_of_odd+n;

print("Sum of Even : " ,sum_of_even);
print("Sum of Odd : " ,sum_of_odd);