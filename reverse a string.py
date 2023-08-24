s = "Hello World!"

print(s[::-1])

print(' '.join(word [::-1] for word in s.split()))


s=s.split()
print(' '.join(reversed(s)))



#output
# !dlroW olleH
# olleH !dlroW
# World! Hello