class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = []

        def helper(index, curr_nums):
            if index > len(candidates):
                return
            
            total = 0
            for n in curr_nums:
                total += n
            
            if total == target:
                self.res.append(curr_nums)
            
            curr_nums.append(candidates[index])
            self.helper(index + 1, curr_nums)
            curr_nums.pop()
            self.helper(index + 1, curr_nums)
        
        helper(0, [])
        return self.res