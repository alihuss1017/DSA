class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
       a = len(nums) - nums.count(val)
       b = [n for n in nums if n!= val]
       nums[0:a] = b
       return a