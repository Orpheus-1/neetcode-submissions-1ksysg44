class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        find if there is a duplicate values
        count each elemment and if there is a duplicate add to counter
        only store non-duplicate values,
        find the max of them

        """
        counter = {}
        maxNum = -1
        for num in nums: # initalizing dictionary
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        for num, count in counter.items(): # logic for determining max
            if count == 1: # if only the value is 1
                maxNum = max(maxNum, num)
        return maxNum
            
            # counter {1: 1 2: 2 3:1}
