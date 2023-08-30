from heapq import heappush, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []

        for count, char in [(-a, 'a'), (-b, 'b'), (-c, 'c')]:
            if count != 0: 
                heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char :
                if not maxHeap:
                    break
                count1, char1 = heappop(maxHeap)
                res += char1
                count1 += 1
                if count1:
                    heappush(maxHeap, (count1, char1))
            else:
                res += char
                count += 1
            if count:
                heappush(maxHeap, (count, char))
        return res

if __name__ == "__main__":
    (testcase1, ans1) = ([1, 1, 7], "ccaccbcc")
    (testcase2, ans2) = ([7, 1, 0] , "aabaa")
    
    sol = Solution()
    assert sol.longestDiverseString(testcase1[0], testcase1[1], testcase1[2]) == ans1, "Testcase 1 failed"
    assert sol.longestDiverseString(testcase2[0], testcase2[1], testcase2[2]) == ans2, "Testcase 2 failed"

    print("All test cases passed Pass")
