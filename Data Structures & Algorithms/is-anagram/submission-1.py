class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letters = dict()

        for char in s:
            letters[char] = letters.get(char, 0) + 1
        
        for char in t:
            if char not in letters:
                return False
            
            letters[char] -= 1
            if letters[char] == 0:
                del letters[char]
        
        if len(letters) == 0:
            return True
        return False
