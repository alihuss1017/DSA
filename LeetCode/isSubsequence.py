class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
       for char in s:
           ind = t.find(char)
           if ind == -1:
               return False
           else: 
               t = t[ind+1:]
       return True