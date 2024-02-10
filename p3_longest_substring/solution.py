"""Includes the Solution class to solve a problem."""


class Solution:
    """Contains functions to solve a problem."""
    # My solution
    def solve1(self, s: str) -> int:
        """Remove from list if already in there else, append and check length."""
        longest = 0
        nonrepeat_substring = []
        for ch in s:
            # If character is already in list, pop until removed.
            while ch in nonrepeat_substring:
                nonrepeat_substring.pop(0)
            nonrepeat_substring.append(ch)

            list_len = len(nonrepeat_substring)
            if  list_len > longest:
                longest = list_len

        return longest
    
        # My solution
    def solve2(self, s: str) -> int:
        """Remove from list if already in there else, append and check length."""
        left = counter = longest = 0
        nonrepeat_substring = {}

        for ch in s:
            if ch in nonrepeat_substring and nonrepeat_substring[ch] == 1:
                while s[left] != ch:
                    nonrepeat_substring[s[left]] = 0
                    left += 1
                    counter -= 1
                nonrepeat_substring[ch] = 0
                left += 1
                counter -= 1
            nonrepeat_substring[ch] = 1
            counter += 1

            longest = max(longest, counter)

        return longest


    # Other's solution
    def other1(self, s: str) -> int:
        """A solution posted by another user."""
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength
    
    # Other's solution
    def other2(self, s: str) -> int:
        """A solution posted by another user."""
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength
    
    # Other's solution
    def other3(self, s: str) -> int:
        """A solution posted by another user."""
        n = len(s)
        maxLength = 0
        charIndex = [-1] * 128
        left = 0
        
        for right in range(n):
            if charIndex[ord(s[right])] >= left:
                left = charIndex[ord(s[right])] + 1
            charIndex[ord(s[right])] = right
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
