class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        for n in nums:
            return max(set(nums), key = nums.count)