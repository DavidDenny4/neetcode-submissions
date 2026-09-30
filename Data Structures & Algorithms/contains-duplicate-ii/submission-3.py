class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        for i in range(len(nums) - k):
            print(f"visited is {visited}")
            for m in range(k):
                if (nums[i + m]) in visited:
                    return True
                visited.add(nums[i + m])
                print(f"visited is now {visited}")
            visited.remove(nums[i])
            print(f"visited is now {visited}")
        return False
