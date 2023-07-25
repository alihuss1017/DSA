class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
       a = list(set(nums))
       a.sort()
       b = len(a)
       nums[0:b] = a
       return b