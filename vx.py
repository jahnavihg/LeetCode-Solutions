from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if total_len > len(s):
            return []

        word_freq = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            current = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    current[word] = current.get(word, 0) + 1
                    count += 1

                    # Too many occurrences of this word
                    while current[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    # All words found
                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                else:
                    current.clear()
                    count = 0
                    left = right

        return result
