from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        ransom = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char in ransom:
            if ransom[char] > magazine_count[char]:
                return False

        return True
