class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = dict()

        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        

        for char in t:
            if char not in char_count:
                return False
            else:
                char_count[char] -= 1

                if char_count[char] == 0:
                    del char_count[char]
        
        return len(char_count) == 0