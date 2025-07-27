class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        strlen = len(s)
        characters = []
        length = 0
        
        for i in range(strlen):
            for j in characters:
                if s[i] == j:
                    return length

            characters.append(s[i])
            length += 1

        return length

print(Solution.lengthOfLongestSubstring("abcdefgha"))