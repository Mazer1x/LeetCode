nums = [-2,1,-3,4,-1,2,1,-5,4]
# Алгоритм Кадане
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        total_sum = nums[0]
        for i in nums[1:]:
            current_sum = max(i, current_sum+i)
            total_sum =  max(total_sum, current_sum)
        return total_sum