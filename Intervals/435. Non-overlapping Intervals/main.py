from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort the intervals based on start values
        intervals.sort(key=lambda a:a[0])

        #Keep track of previous end value
        prevEnd = intervals[0][1]

        #Define answer
        answer = 0
        
        
        #Loop over intervals
        for i in range(1, len(intervals)):
            #If the current interval overlaps with prevEnd
            if intervals[i][0] < prevEnd:
                #Update the prevEnd as minimum of prevEnd and current interval's end
                prevEnd = min(prevEnd, intervals[i][1])
                #Increment answer
                answer += 1
            #Else
            else:
                #Update the prevEnd as current interval's end
                prevEnd = intervals[i][1]
            
        return answer


        

if __name__ == "__main__":
    (testcase1, ans1) = ([[1,2],[2,3],[3,4],[1,3]], 1)
    (testcase2, ans2) = ([[1,2],[1,2],[1,2]], 2)
    (testcase3, ans3) = ([[1,2],[2,3]], 0)
    
    sol = Solution()
    assert sol.eraseOverlapIntervals(testcase1) == ans1, "Testcase 1 failed"
    assert sol.eraseOverlapIntervals(testcase2) == ans2, "Testcase 2 failed"
    assert sol.eraseOverlapIntervals(testcase3) == ans3, "Testcase 3 failed"

    print("All test cases passed Pass")