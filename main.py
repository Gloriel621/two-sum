
import numpy as np
def twoSum(nums: list, target: int):

    length = len(nums)

    for i in range(length):
        for j in range(i+1, length):
            if nums[i] + nums[j] == target:
                n = nums[i]
                m = nums[j]
                break 
    
    # if n != m, then find the indexes by .index()
    if n != m:
        return [nums.index(n), nums.index(m)]
    
    # if n == m, then find the first two indexes of n and return
    else:
        x = np.where(np.array(nums)==n)[0]
        x = list(x)
        return x[:2]
    
# Assumption
# There is always two a, b in list nums that meet a + b = target

