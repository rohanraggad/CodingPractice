def quick_select(left,right):
    pivot_element_value, p = nums[right], left 
    for i in range(left,right):
        if nums[i]<= pivot_element_value:
            p+=1
    # nums[p],nums[nums.index(pivot_element_value)] = nums[nums.index(pivot_element_value)], nums[p]
    nums[p], nums[right] = nums[right],nums[p]
    if k > p:
        return quick_select(p+1,right)
    elif k < p:
        return quick_select(left,p-1)
    else:
        return nums[p]


k = eval(input())
nums = [eval(i) for i in input().split(" ")]
nums = list(set(nums))
k = len(nums) - k
print(quick_select(0,len(nums)-1))
