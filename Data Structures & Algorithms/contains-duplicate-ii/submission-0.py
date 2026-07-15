class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        for i in range(len(nums) - k):
            for m in range(k):
                if (nums[i + m]) in visited:
                    return True
                visited.add(nums[i + m])
            visited.remove(nums[i])
        return False
