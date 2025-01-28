n = int(input("Enter the number for Fibonacci "))
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))
print("***************************************************************************************************************")
n1 = int(input("Enter the number for Factorial "))
def Factorial(n1):
    if n1 == 1 or n1 == 2:
        return n1
    else:
        return n1*Factorial(n1-1)


print(Factorial(n1))
print("***************************************************************************************************************")
n2 = int(input("Enter the number for sum "))
def sum(n2):
    if n2 == 0 or n2 == 1:
        return n2
    else:
        return n2 + sum(n2-1)


print(sum(n2))
print("***************************************************************************************************************")
n3 = int(input("Enter the base "))
p = int(input("Enter the power "))
def power(n3,p):
    if p == 0:
        return 1
    elif p == 1:
        return n3
    else:
        return n3**p


print(power(n3,p))
#HW(19.11.24)
print("***************************************************************************************************************")
N=int(input("Enter the base: "))
P = int(input("Enter the power: "))
def power(N, P):
	if P == 0:
		return 1
	return (N*power(N, P-1))

print(power(N,P))