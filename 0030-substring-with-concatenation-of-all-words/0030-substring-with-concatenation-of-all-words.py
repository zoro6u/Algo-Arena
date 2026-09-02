from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not words[0]:
            return []

        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        n = len(s)

        if total_len > n:
            return []

        target_count = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            count = Counter()
            words_in_window = 0

            for right in range(offset, n - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word in target_count:
                    count[word] += 1
                    words_in_window += 1

                    while count[word] > target_count[word]:
                        left_word = s[left:left + word_len]
                        count[left_word] -= 1
                        words_in_window -= 1
                        left += word_len

                    if words_in_window == num_words:
                        result.append(left)
                        left_word = s[left:left + word_len]
                        count[left_word] -= 1
                        words_in_window -= 1
                        left += word_len
                else:
                    count.clear()
                    words_in_window = 0
                    left = right + word_len

        return sorted(result)