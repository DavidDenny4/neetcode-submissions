class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for oper in operations:
            print(oper)
            if oper == "+":
                results.append(results[-1] + results[-2])
            elif oper == "C":
                results.pop()
            elif oper == "D":
                results.append(results[-1] * 2)
            else:
                results.append(int(oper))
        
        sum = 0
        for i in results:
            sum += i
        
        return sum