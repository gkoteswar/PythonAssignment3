
def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact*=i
    return fact

num = input("Enter a number: ")
print(f"Factorial of {num} is:",factorial(int(num)))