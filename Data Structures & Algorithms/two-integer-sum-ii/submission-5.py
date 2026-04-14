class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        L, R = 0, n-1
        while L < R: 
            if numbers[L] + numbers[R] == target:
                break
            if numbers[L] + numbers[R] < target:
                L += 1
            else:
                R -=1
        return [L+1, R+1]

    