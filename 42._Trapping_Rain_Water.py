# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:
class Solution:
    def trap(self, height: list[int]) -> int:
        data=[0 for i in range(len(height))]
        c=0
        front=[height[0]]
        back=[height[-1]]
        r=len(height)
        for i in range(1,len(height)):
            front.append(max(front[i-1],height[i]))
            back.append(max(back[i-1],height[-1*(i+1)]))
        for i in range(len(height)):
            m=min(front[i],back[-1*(i+1)])-height[i]
            c+=m
        return c

# Another way:
class Solution:
    def trap(self, height: list[int]) -> int:
        n=len(height)
        m=height[0]
        left=[m]
        for i in range(1,n):
            if height[i]>m:
                m=height[i]
            if m>height[i]:
                left.append(m)
            else:
                left.append(height[i])
        m=height[-1]
        right=[m]
        for i in range(n-2,-1,-1):
            if height[i]>m:
                m=height[i]
            if m>height[i]:
                right.append(m)
            else:
                right.append(height[i])
        right=right[::-1]
        ans=[0]*n
        for i in range(n):
            ans[i]=min(left[i],right[i])-height[i]
        return sum(ans)  