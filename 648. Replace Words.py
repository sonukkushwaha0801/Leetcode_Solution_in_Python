# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:


from typing import List


class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEndOfWord = True

    def search(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isEndOfWord

    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

    def findShortedPrefix(self, word):
        curr = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return word
            curr = curr.children[index]
            if curr.isEndOfWord:
                return word[:i + 1]
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        tokens = sentence.split()
        result = []
        for token in tokens:
            prefix = trie.findShortedPrefix(token)
            result.append(prefix)
        return ' '.join(result)
    


# Another way to solve this:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def search_root(self, word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.is_end:
                return prefix
        return word
    
    def replaceWords(self, dictionary, sentence):
        for word in dictionary:
            self.insert(word)
        
        words = sentence.split()
        replaced_words = [self.search_root(word) for word in words]
        
        return " ".join(replaced_words)