class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.res = []

        def helper(index, curr_nums):
            
            total = 0
            for n in curr_nums:
                total += n
            
            if total == target:
                self.res.append(curr_nums.copy())
                return

            if index >= len(candidates) or total > target:
                return
            
            curr_nums.append(candidates[index])
            helper(index + 1, curr_nums)
            curr_nums.pop()
            while (index + 1) < len(candidates) and candidates[index + 1] == candidates[index]:
                index += 1
            helper(index + 1, curr_nums)
        
        helper(0, [])
        return self.res