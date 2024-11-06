#Merge Sorted Array
import unittest

class Solution:
    def merge(self, nums1, m, nums2, n):
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

class TestSolution(unittest.TestCase):
    def test_merge(self):
        sol = Solution()

        nums1 = [1, 2, 3, 0, 0, 0]
        sol.merge(nums1, 3, [2, 5, 6], 3)
        self.assertEqual(nums1, [1, 2, 2, 3, 5, 6])

        nums1 = [1]
        sol.merge(nums1, 1, [], 0)
        self.assertEqual(nums1, [1])

        nums1 = [0]
        sol.merge(nums1, 0, [1], 1)
        self.assertEqual(nums1, [1])

        nums1 = [4, 5, 6, 0, 0, 0]
        sol.merge(nums1, 3, [1, 2, 3], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

        nums1 = [2, 4, 6, 0, 0, 0]
        sol.merge(nums1, 3, [1, 3, 5], 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()
