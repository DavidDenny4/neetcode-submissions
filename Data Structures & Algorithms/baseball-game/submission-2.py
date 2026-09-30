class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for oper in operations:
            if oper.isdigit():
                results.append(int(oper))
            if oper == "+":
                results.append(results[-1] + results[-2])
            if oper == "C":
                results.remove(len(results) - 1)
            if oper == "D":
                results.append(results[-1] * 2)
        
        sum = 0
        for i in results:
            sum += i
        
        return sum