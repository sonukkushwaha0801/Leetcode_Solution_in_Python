# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res=[]
        def dfs(candidates,target,path,res):
            if target==0:
                res.append(path)
                return
            for i in range(len(candidates)):
                if candidates[i]>target:
                    continue
                dfs(candidates[i:],target-candidates[i],path+[candidates[i]],res)
        dfs(candidates,target,[],res)
        return res

# Another way:
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans=[]
        l=[]
        Combinations(0,target,candidates,ans,l)
        return ans

def Combinations(index,target,candidates,ans,l):
    if index == len(candidates):
        if target == 0:
            ans.append(l[:])
        return 

    if candidates[index]<= target:
        l.append(candidates[index])
        Combinations(index, target-candidates[index] , candidates, ans, l)
        l.pop()

    Combinations(index+1, target, candidates,ans , l)

    
        