class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setQ = []
        maxa = 0
        for char in s:
            
            if char not in setQ:
                setQ.append(char)
                maxa = max(maxa, len(setQ))
            else:
                while setQ[0] != char:
                    setQ = setQ[1:]
                setQ = setQ[1:]
                setQ.append(char)


        return maxa