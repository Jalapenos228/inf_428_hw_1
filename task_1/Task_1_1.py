# Longest Continuous Increasing Subsequence
import unittest

class Solution:
    def findLengthOfLCIS(self, nums):
        result = 0
        anchor = 0

        for i in range(len(nums)):
            if i > 0 and nums[i-1] >= nums[i]:
                anchor = i
            result = max(result, i - anchor + 1)

        return result

class TestSolution(unittest.TestCase):

    def test_findLengthOfLCIS(self):
        sol = Solution()

        self.assertEqual(sol.findLengthOfLCIS([1, 3, 5, 4, 7]), 3)
        self.assertEqual(sol.findLengthOfLCIS([2, 2, 2, 2, 2]), 1)
        self.assertEqual(sol.findLengthOfLCIS([1, 2, 3, 4, 5]), 5)
        self.assertEqual(sol.findLengthOfLCIS([5, 4, 3, 2, 1]), 1)
        self.assertEqual(sol.findLengthOfLCIS([1, 2, 0, 3, 5, 6, 7, 8]), 6)

if __name__ == '__main__':
    unittest.main()
