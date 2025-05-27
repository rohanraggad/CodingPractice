def max_min():
    maximum,minimum = 0,1000000
    for i in nums:
        if i > maximum:
            maximum = i 
        if i < minimum:
            minimum = i 
    return maximum,minimum

nums = [eval(i) for i in input().split(" ")]
ans = max_min()
print(ans[0],ans[1])