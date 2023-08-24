def binarySearch(num, target):
    left = 0
    right = len(num) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == num[mid]:
            return mid
        elif num[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

num = [25, 11, 16, 15, 24]
num.sort()
print("Sorted list:", num)
target = 15
res = binarySearch(num, target)

if res != -1:
    print(f"The value {target} found at index {res}")
else:
    print(f"The value {target} is not found")
