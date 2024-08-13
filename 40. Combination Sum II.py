# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:

from typing import List


class Solution(object):
    def combinationSum2(self, candidates, target):
        sum2combination=[]
        sizeCandidates=len(candidates)
        candidates.sort()
        def solve(idx,candidateList,sum): 
            if sum==target:
                sum2combination.append(candidateList)
                return 
            for candidate in range(idx,sizeCandidates):
                candidatesTraverse=candidates[candidate]
                sumCandidates=sum+candidatesTraverse
                if candidate>idx and candidatesTraverse==candidates[candidate-1]:
                    continue
                if sumCandidates>target:
                    break
                solve(candidate+1,candidateList+[candidatesTraverse],sumCandidates)
        solve(0,[],0)
        return sum2combination
        
# Another way:
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() 
        result = []
        
        def backtrack(start, target, current):
            if target == 0:
                result.append(list(current))
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break 
                current.append(candidates[i])
                backtrack(i + 1, target - candidates[i], current) 
                current.pop() 
        
        backtrack(0, target, [])
        return result