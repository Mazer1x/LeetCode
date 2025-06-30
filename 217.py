# Without using set()
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            if i in dictionary.keys():
                return True
            else:
                dictionary[i]=1
        return False

#Using set()
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            else:
                hash_set.add(i)
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums)!=len(set(nums)):return True
        else: return False