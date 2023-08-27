from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False

if __name__ == "__main__":
    (testcase1, ans1) = ([1,2,3,1], True)
    (testcase2, ans2) = ([1,2,3,4], False)
    (testcase3, ans3) = ([1,1,1,3,3,4,3,2,4,2], True)
    
    sol = Solution()
    assert sol.containsDuplicate(testcase1) == ans1, "Testcase 1 failed"
    assert sol.containsDuplicate(testcase2) == ans2, "Testcase 2 failed"
    assert sol.containsDuplicate(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")

