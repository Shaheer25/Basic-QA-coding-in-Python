def linearSearch(num,target):
    for i in range (len(num)):
        if num[i]==target:
            return i
    return -1


num=[10,56,89,4,8,99]
print(num)
target = int(input("\nenter the element you want to search"))

result = linearSearch(num,target)

if result != -1:
    print(f"{target} is  found at {result+1}")
else:
    print(f"{target} is not found in {num}")
