class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gasNo = 0
        costNo = 0
        total = 0
        
        while gasNo < len(gas) and costNo < len(cost):
            if cost[costNo] < gas[gasNo]:
                total = gas[gasNo] - cost[costNo]
                
                if total < 0:
                    return (-1)
                gasNo += 1
                costNo += 1
                else :
                    total = total + gas[gasNo] + cost[costNo]
        return total
        
            
        
        
        