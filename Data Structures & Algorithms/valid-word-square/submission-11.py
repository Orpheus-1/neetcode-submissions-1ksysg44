class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)
        for col in range(n):
            word = ""
            for row in range(len(words)):
                if col < len(words[row]):
                    word += words[row][col]
            if word != words[col]:
                return False
            
        
        return True