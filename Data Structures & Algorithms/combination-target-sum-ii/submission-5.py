class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.res = set()

        def helper(index, curr_nums):
            
            total = 0
            for n in curr_nums:
                total += n
            
            if total == target:
                self.res.add(curr_nums.copy())

            if index >= len(candidates):
                return
            
            curr_nums.append(candidates[index])
            helper(index + 1, curr_nums)
            curr_nums.pop()
            helper(index + 1, curr_nums)
        
        helper(0, [])
        return list(self.res)