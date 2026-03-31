class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        occurence = {}

        for char in s:
            occurence[char] = occurence.get(char, 0) + 1

        for char in t:
            if char not in occurence:
                return False
            
            occurence[char] -= 1

            if occurence[char] == 0:
                del occurence[char]
        
        return len(occurence) == 0

