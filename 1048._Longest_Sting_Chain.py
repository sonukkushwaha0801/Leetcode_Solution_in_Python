# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in range(len(w)))
        return max(dp.values())
    
# Second Way:
class Solution:
    def __init__(self):
        self.chain_lengths = {}
        self.word_set = {}

    def calculate_chain_length(self, word) -> int:
        # If the word doesn't exist in the set
        if word not in self.word_set or not self.word_set[word]:
            return 0

        # If chain length for the word is already calculated
        if word in self.chain_lengths:
            return self.chain_lengths[word]

        chain_length = 1

        # Try removing one character at a time from the word and calculate chain length
        for i in range(len(word)):
            new_word = word[:i] + word[i + 1:]
            chain_length = max(chain_length, 1 + self.calculate_chain_length(new_word))

        self.chain_lengths[word] = chain_length
        return chain_length

    def longestStrChain(self, words) -> int:
        for word in words:
            self.word_set[word] = True

        max_chain_length = -1

        # Calculate the maximum chain length for each word
        for word in words:
            max_chain_length = max(max_chain_length, self.calculate_chain_length(word))

        return max_chain_length