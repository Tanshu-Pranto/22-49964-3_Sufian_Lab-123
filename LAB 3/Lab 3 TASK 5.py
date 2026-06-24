
n = int(input("Enter the limit : "))
a, b = 0, 1
print(f"Fibonacci numbers below {n}:")

while a < n:
    print(a, end=" ")
    a, b = b, a + b
print() 