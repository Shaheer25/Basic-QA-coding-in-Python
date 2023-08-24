limit =5
print("Even")
for i in range (2 , limit ,2):
    print(i)
print("odd")
for i in range (1,limit,2):
    print(i)

def isprime(num):
    if num % 2 == 0 :
        print("EVEN")
    else :
        print("ODD")

isprime(20)
isprime(21)


# o/p:
# Even
# 2
# 4
# odd
# 1
# 3
# EVEN
# ODD