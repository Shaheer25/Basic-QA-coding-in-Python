def linearSearch(target,num):
  for i in range(len(num)):
    if num[i]==target:
      return i 
  return -1
  
  
num = [25, 11, 16, 15, 24]
target = 16
res= linearSearch(target,num)

if res != -1:
    print(f"The value {target} found at index {res}")
else:
    print(f"The value {target} is not found")
