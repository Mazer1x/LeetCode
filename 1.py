class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # Значение - индекс
        for ind, value in enumerate(nums):
            if (target-nums[ind]) in hash_map:
                return([hash_map[target-nums[ind]],ind])
            hash_map[value] = ind