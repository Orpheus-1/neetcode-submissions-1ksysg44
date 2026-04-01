class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}
        i = 0
        for i in nums:
            print(dupes)
            if i in dupes:
                return True
            else: 
                dupes[i] = 1
        print("Non-Duplicate Final Dictionary: ")
        print(dupes)
        return False
            
        