# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: list[str]) -> int:
        wordlist = set(wordlist)
        if endWord not in wordlist:
            return 0

        if beginWord not in wordlist:
            wordlist.add(beginWord)

        # Prefix -> Postfix -> Letter mapping

        pref_post_lett = {}
        for index in range(len(beginWord)):
            for word in wordlist:
                pref = word[:index]
                post = word[1+index:]
                lett = word[index]

                if pref not in pref_post_lett:
                    pref_post_lett[pref] = {}

                if post not in pref_post_lett[pref]:
                    pref_post_lett[pref][post] = set()

                if lett not in pref_post_lett[pref][post]:
                    pref_post_lett[pref][post].add(lett)


        adj = {}
        
        for w in wordlist:
            adj[w] = []

        # Building adjacency map

        for pref in pref_post_lett:
            post_lett = pref_post_lett[pref]

            for post in post_lett:
                lett = post_lett[post]

                for l1 in lett:
                    for l2 in lett:
                        if l1 != l2:
                            w1 = pref + l1 + post
                            w2 = pref + l2 + post

                            adj[w1].append(w2)

        wave = deque([(beginWord, 1)])
        visited = set()

        while len(wave) > 0:
            node = wave.popleft()

            wrd = node[0]
            stp = node[1]

            if wrd == endWord:
                return stp

            if wrd in visited:
                continue
            
            visited.add(wrd)

            for nbr in adj[wrd]:
                if nbr not in visited:
                    wave.append((nbr, stp + 1))

        return 0
        
# Another way:
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: list[str]) -> int:
        def isNeighbour(word1, word2):
            count = 0
            for i, letter in enumerate(word1):
                if letter!=word2[i]:
                    count+=1
                if count>1:
                    return False
            return True
        wordSet = set(wordlist)
        if endWord not in wordSet:
            return 0
        queue1 = deque([beginWord])
        queue2 = deque([endWord])
        visited1 = set([beginWord])
        visited2 = set([endWord])
        level = 1
        while queue1 and queue2:
            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1
                visited1, visited2 = visited2, visited1
            n = len(queue1)
            for _ in range(n):
                node = queue1.popleft()
                if node in visited2:
                    return level
                for word in wordSet:
                    if word not in visited1 and isNeighbour(node,word):
                        queue1.append(word)
                        visited1.add(word)
            level += 1
        return 0