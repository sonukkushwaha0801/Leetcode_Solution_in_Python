# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWordCompleted = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                newRoot.children[alphabetIndex] = TrieNode()
            newRoot = newRoot.children[alphabetIndex]
        newRoot.isWordCompleted = True
    
    def search(self, word: str) -> bool:
        newRoot = self.root
        for ch in word:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                return False
            newRoot = newRoot.children[alphabetIndex]
        if newRoot.isWordCompleted == True:
            return True
        return False
    
    def startsWith(self, prefix: str) -> bool:
        newRoot = self.root
        for ch in prefix:
            alphabetIndex = ord(ch) - ord('a')
            if newRoot.children[alphabetIndex] == None:
                return False
            newRoot = newRoot.children[alphabetIndex]
        return True
    
# Another way:
class Node:
    
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    
    def contains_key(self,ch):
        return self.links[ord(ch)-97]!=None
    
    def put(self,ch,node):
        self.links[ord(ch)-97]=node
        
    def get(self,ch):
        return self.links[ord(ch)-97]
    
    def set_end(self):
        self.flag=True
        
    def isEnd(self):
        return self.flag

class Trie:

    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch,Node())
            node=node.get(ch)
        node.set_end()

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                return False
            node=node.get(ch)
        return node.isEnd()
        

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if not node.contains_key(ch):
                return False
            node=node.get(ch)
        return True