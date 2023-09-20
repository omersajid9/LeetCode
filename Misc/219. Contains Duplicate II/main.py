from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and 0 < abs(i-j) <= k:
                    return True

        return False
    
if __name__ == "__main__":
    (testcase1, ans1) = ([[1,2,3,1], 3], True)
    (testcase2, ans2) = ([[1,0,1,1], 1], True)
    (testcase3, ans3) = ([[1,2,3,1,2,3], 2], False)
    
    sol = Solution()
    assert sol.containsNearbyDuplicate(*testcase1) == ans1, "Testcase 1 failed"
    assert sol.containsNearbyDuplicate(*testcase2) == ans2, "Testcase 2 failed"
    assert sol.containsNearbyDuplicate(*testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")