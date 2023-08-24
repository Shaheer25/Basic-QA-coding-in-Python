def findSecondLargest(num):

    if len(num) < 2 :
        print("The Length Should be more than 2")
        return  False

    largest = float()
    secondLargest= float()

    for num in num :
        if num > largest:
            secondLargest = largest
            largest = num
        elif num > secondLargest and num != largest :
            secondLargest=num

    return secondLargest

print(findSecondLargest([10,80,74,68,69,100,88,72]))