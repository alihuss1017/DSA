class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        first_word = strs[0]
        ans = ""
        phrase = ""
        for letter in first_word:
            phrase += letter
            for word in strs[1:]:
                if not word.startswith(phrase):
                    return ans
            ans += letter
        
        return ans