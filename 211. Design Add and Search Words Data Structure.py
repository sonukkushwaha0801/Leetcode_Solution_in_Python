# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class TrieNode:
    def __init__(self):
        self.links = {}
        self.end = False
    
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.maxL = 0
        
    def addWord(self, word):
        node = self.root
        l = 0
        for w in word:
            if w not in node.links:
                node.links[w] = TrieNode()
            node = node.links[w]
            l += 1
        
        self.maxL = max(self.maxL, l)
        node.end = True

    def search(self, word):
        if len(word) > self.maxL:
            return False
        
        def helper(index, node):
            for inn in range(index, len(word)):
                c = word[inn]
                if c == ".":
                    for child in node.links.values():
                        if helper(inn+1, child):
                            return True
                    return False
                else:
                    if c not in node.links:
                        return False
                    node = node.links[c]

            return node.end
        return helper(0, self.root)
