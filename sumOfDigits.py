def sum_of_digits(num):
    digit_sum = 0
    

    num_str = str(num)
    
    for digit in num_str:
        digit_sum += int(digit)
    
    return digit_sum

num = int(input())

result = sum_of_digits(num)
print( result)
