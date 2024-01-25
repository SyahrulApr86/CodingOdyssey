# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
from typing import List


class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        n1 = len(arr1)
        n2 = len(arr2)
        arr3 = [0] * (n1 + n2)
        i = 0
        j = 0
        k = 0

        # Traverse both array
        while i < n1 and j < n2:
            if arr1[i] < arr2[j]:
                arr3[k] = arr1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = arr2[j]
                k = k + 1
                j = j + 1

        while i < n1:
            arr3[k] = arr1[i];
            k = k + 1
            i = i + 1

        while j < n2:
            arr3[k] = arr2[j];
            k = k + 1
            j = j + 1

        if (n1 + n2) % 2 == 1:
            return arr3[(n1 + n2) // 2]
        else:
            return (arr3[(n1 + n2) // 2] + arr3[(n1 + n2) // 2 - 1]) / 2

#
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         if len(nums1) > len(nums2):
#             nums1, nums2 = nums2, nums1
#
#         x, y = len(nums1), len(nums2)
#         start = 0
#         end = x
#
#         while start <= end:
#             partitionX = (start + end) // 2
#             partitionY = (x + y + 1) // 2 - partitionX
#
#             maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
#             minRightX = float('inf') if partitionX == x else nums1[partitionX]
#
#             maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
#             minRightY = float('inf') if partitionY == y else nums2[partitionY]
#
#             if maxLeftX <= minRightY and maxLeftY <= minRightX:
#                 if (x + y) % 2 == 0:
#                     return max(maxLeftX, maxLeftY) / 2.0 + min(minRightX, minRightY) / 2.0
#                 else:
#                     return max(maxLeftX, maxLeftY)
#             elif maxLeftX > minRightY:
#                 end = partitionX - 1
#             else:
#                 start = partitionX + 1

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         nums = sorted(nums1 + nums2)
#         size = len(nums)
#         if size % 2 == 0:
#             n1 = nums[size // 2 - 1]
#             n2 = nums[size // 2]
#             return (n1 + n2) / 2
#         return nums[size // 2]

A = Solution()
A.findMedianSortedArrays([1, 2,3,4,5], [6,7,8,9,10])
