from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        groups = defaultdict(list)  # Dictionary to collect groups

        for s in strings:
            key = self._get_shift_pattern(s)  # Convert string to shift pattern
            groups[key].append(s)             # Group by that pattern

        return list(groups.values())          # Return the grouped lists

    def _get_shift_pattern(self, s):
        if len(s) == 1:
            return (-1,)  # single letter — just group them together

        pattern = []
        for i in range(1, len(s)):
            # Use modulo 26 to handle wraparound like z → a
            diff = (ord(s[i]) - ord(s[i - 1])) % 26
            pattern.append(diff)
        return tuple(pattern)  # tuples can be used as dict keys
