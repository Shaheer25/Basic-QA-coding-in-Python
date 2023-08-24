def bubbleSort(num):
    n=len(num)

    for i in range (n):
        swapped = False

        for j in range (0, n-i-1):
            if num[j]>num[j+1]:
                num[j]=num[j+1]
                num[j+1]=num[j]
                swapped=True

        if not swapped:
            break

num = [78,55,67,99,15,86,67,19]

print("original:",num)
bubbleSort(num)
print("sorted:",num)


# o/p:
# original: [78, 55, 67, 99, 15, 86, 67, 19]
# sorted: [15, 15, 15, 15, 15, 19, 19, 19]