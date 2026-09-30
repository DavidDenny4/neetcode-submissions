class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for oper in operations:
            if oper == "+":
                results.append(results[-1] + results[-2])
            if oper == "C":
                results.pop()
            if oper == "D":
                results.append(results[-1] * 2)
            results.append(int(oper))
        
        sum = 0
        for i in results:
            sum += i
        
        return sum