def fibonacci(n):
    a = 0;
    b = 1;
    for i in range(n):
        print(a,end=" ");
        a = b;
        b= a + b;

num = int(input("Enter the number of terms: "));

print(f"Fibonacci numbers of {num}:");
fibonacci(num);
