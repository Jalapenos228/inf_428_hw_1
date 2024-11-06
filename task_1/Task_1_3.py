#Intersection of Two Arrays
import unittest

class Solution:
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        result = []
        for n in nums2:
            if n in seen:
                result.append(n)
                seen.remove(n)
        return result

class TestSolution(unittest.TestCase):
    def test_intersection(self):
        sol = Solution()

        self.assertEqual(sorted(sol.intersection([1, 2, 2, 1], [2, 2])), [2])
        self.assertEqual(sorted(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4])), [4, 9])
        self.assertEqual(sol.intersection([1, 3, 5], [2, 4, 6]), [])
        self.assertEqual(sol.intersection([], []), [])
        self.assertEqual(sol.intersection([1, 2, 3], []), [])
        self.assertEqual(sorted(sol.intersection([1, 2, 3], [1, 2, 3])), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()
