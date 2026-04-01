class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        """ 
        soln = {}
        combined = s + t
        for char in combined:
            if char.isalpha(): 
                soln[char] = soln.get(char, 0) + 1
        for char in soln: 
            if soln[char] % 2 != 0:
                return False
        return True
        """
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


        