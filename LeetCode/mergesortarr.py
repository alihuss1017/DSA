class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.reverse()
        for i in range(len(nums2)):
            if nums1[i] == 0:
                nums1[i] = nums2[i]
            else:
                break
        nums1.sort()
            