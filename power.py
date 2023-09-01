def power_two(n):
    if n<=0:
        return False
    else :
        return n&(n-1)==0

def power_three(n):
    if n<=0:
        return False
    else :
        while n%3==0:
            n/=3
        return n==1

def power_five(n):
    if n<=0:
        return False
    else :
        while n%5==0:
            n/=5
        return n==1


n=int(input())
if power_two(n):
   print(f"{n} is a power of 2")
elif power_three(n):
    print(f"{n} is a power of 3")
elif power_five(n):
    print(f"{n} is a power of 5")
else :
    print(f"{n} is not the power of 2/3")
