class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,j in enumerate(nums):
            for l,k in enumerate(nums):
                if (i != l and j + k == target):
                    return [i,l]