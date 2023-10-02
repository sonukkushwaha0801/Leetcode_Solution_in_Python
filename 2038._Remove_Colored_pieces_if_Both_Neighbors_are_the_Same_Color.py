# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# One way:
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_A = 0
        count_B = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    count_A += 1
                else:
                    count_B += 1
        return count_A > count_B

# Another Way:
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        count_A = sum(1 for i in range(1, len(colors) - 1) if colors[i - 1] == colors[i] == colors[i + 1] == 'A')
        count_B = sum(1 for i in range(1, len(colors) - 1) if colors[i - 1] == colors[i] == colors[i + 1] == 'B')
        return count_A > count_B
