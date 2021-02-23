# Given an array of integers, determine whether the array is monotonic or not.
A = [6, 5, 4, 4] 

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(solution(A)) 
