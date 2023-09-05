def count(num):
  z_count=0
  
  digit = str(num)
  
  for res in digit:
    if '0' in res :
      z_count+=1
  return z_count
num = int(input())

res=count(num)

print(res)
