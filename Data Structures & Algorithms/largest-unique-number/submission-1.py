class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        """
        use the max function to find the largest value in the set.
        need to iterate on it to make it so that only if it duplicates, so maybe we can instead use a dictionary
        dictionary stores key : value pair, find the key with the largest amount buy only one occurance
        """
        freq_map = Counter(nums)


        return max((num for num, freq in freq_map.items() if freq == 1),
            default =-1,
            )
        