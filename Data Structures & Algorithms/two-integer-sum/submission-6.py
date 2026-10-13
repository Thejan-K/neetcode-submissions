class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset=set()
        
        for num in nums:
            hashset.add(num)
        for i in range(len(nums)):
            if target-nums[i] in hashset and nums.index(target-nums[i])!=i:
                answers=[i, nums.index(target-nums[i])]
                return sorted(answers)
                
