class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        p1 = 0
        p2 = 1
        
        while p1 < len(temperatures)-1:

            if p2 < len(temperatures) and temperatures[p2] <= temperatures[p1]:
                p2+=1
                continue
            else:
                if p2 < len(temperatures):
                    temperatures[p1] = p2-p1
                else:
                    temperatures[p1] = 0

                
                p1+=1
                p2=p1+1
        
        temperatures[-1] = 0
        return temperatures
