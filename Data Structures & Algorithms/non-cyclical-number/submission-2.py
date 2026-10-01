class Solution:
    def isHappy(self, n: int) -> bool:
        
        computed = set()

        def nonCycle(num):
            
            if num in computed:
                return False
            
            computed.add(num)
            sum = 0
            digits = [int(d) for d in str(num)]
            for d in digits:
                sum += d ** 2
            
            if sum == 1:
                return True
            nonCycle(sum)
        
        return nonCycle(n)
