class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        subset = set
        
        def helper(index, curr_set):
            if index == len(nums):
                subset.add(curr_set.copy())
                return
            
            curr_set.append(nums[index])
            helper(index + 1, curr_set)
            curr_set.pop()
            helper(index + 1, curr_set)
        
        helper(0, [])
        for sub in subset:
            print(f"sub is {sub}")
            total += sum(sub)
        
        return total