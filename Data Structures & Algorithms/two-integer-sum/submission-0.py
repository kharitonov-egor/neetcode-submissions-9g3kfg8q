class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        usedSet = set()

        for i in range(len(nums)):



            diffrenece = target - nums[i]

            if diffrenece in usedSet:
                return [nums.index(diffrenece),i]
            
            usedSet.add(nums[i])

        