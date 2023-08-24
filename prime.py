def isprime(num):
    if num == 0 :
        return False
    for i in range (2, int(num **0.5)+1):
        if num % i == 0 :
            return False
    return True

print("The prime Numbers are")
for i in range(100):
    if isprime(i):
        print(i, end = "\n")

print()

if isprime(10):
   print("Is a prime")
else :
    print("not a prime")