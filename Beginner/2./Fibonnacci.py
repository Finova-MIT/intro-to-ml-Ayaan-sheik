n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci sequence:", a)
else:
    print("Fibonacci sequence:", end=" ")
    while count < n:
        print(a, end=" ")  
        temp = a + b  
        a = b  
        b = temp
        count += 1  