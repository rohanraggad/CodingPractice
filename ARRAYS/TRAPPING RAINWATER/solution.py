def brute_force_approach(heights):
    total_trapped_water = 0
    for i in range(1,len(heights)-1):
        left = heights[0:i]
        right = heights[i+1:]
        left_max = max(left)
        right_max = max(right)
        if min(left_max,right_max) - heights[i] >= 0:
            total_trapped_water += min(left_max,right_max) - heights[i]
    return total_trapped_water

def precalculate_left_right_max(heights):
    total_trapped_water = 0
    left_max = [0 for i in range(len(heights))]
    left_max[0] = heights[0] # as there is no block in the left of first block
    right_max = [0 for i in range(len(heights))]
    right_max[len(right_max)-1] = heights[len(heights)-1] # as there is no block in the right of last block

    for i in range(1,len(heights)):
        left_max[i] = max(heights[i],left_max[i-1])
    for i in range(len(heights)-2,-1,-1):
        right_max[i] = max(right_max[i+1],heights[i])

    for i in range(len(heights)):
        if min(left_max[i],right_max[i]) - heights[i] > 0:
            total_trapped_water += min(left_max[i],right_max[i]) - heights[i]
    return total_trapped_water
    

if __name__ == "__main__":
    heights = [eval(i) for i in input().split(',')]
    print(brute_force_approach(heights))
    print(precalculate_left_right_max(heights))