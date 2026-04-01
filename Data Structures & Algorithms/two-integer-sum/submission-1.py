class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i, n in enumerate(nums):
            difference = target - nums[i]
            if difference in ans:
                return [ans[difference], i]
            else: 
                ans[n] = i
        