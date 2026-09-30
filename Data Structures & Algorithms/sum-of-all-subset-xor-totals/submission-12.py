class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        subset = []
        
        def helper(index, curr_set):
            if index == len(nums):
                subset.append(curr_set.copy())
                return
            
            curr_set.append(nums[index])
            helper(index + 1, curr_set)
            curr_set.pop()
            helper(index + 1, curr_set)
        
        helper(0, [])
        print(f"subsets are {subset}")

        subsets = set()
        for sub in subset:
            if sub not in subsets:
                total += sum(sub)
            subsets.add(sub)
        return total