class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        maxa = 0

        for i in range(len(s)):

            if s[i] not in seen:
                seen.append(s[i])
                maxa = max(maxa, len(seen))
            else:
                while s[i] != seen[0]:
                    seen=seen[1:]
                seen=seen[1:]
                seen.append(s[i])
        return maxa
            
