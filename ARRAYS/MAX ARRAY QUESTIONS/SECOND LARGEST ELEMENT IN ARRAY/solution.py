def second_largest():
    largest,second_largest = 0,0
    for i in nums:
        if i > largest:
            second_largest = largest
            largest = i 
        if i > second_largest and i != largest:
            second_largest = i 
    return second_largest
nums = [eval(i) for i in input().split(" ")]
print(second_largest())