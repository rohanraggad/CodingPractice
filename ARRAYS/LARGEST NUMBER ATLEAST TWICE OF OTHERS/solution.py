def dominantIndex(nums):
    maximum = max(nums)
    for i in nums:
        if i == maximum:
            continue
        if 2*i > maximum:
            return -1
    return nums.index(maximum)

if __name__ == "__main__":
    print(dominantIndex([0,0,0,0]))