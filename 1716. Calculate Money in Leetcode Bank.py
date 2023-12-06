# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
#type first
class Solution(object):
    def totalMoney(self, n):
        week_count = n // 7
        remaining_days = n % 7
        
        total = ((week_count * (week_count - 1)) // 2) * 7 
        total += week_count * 28
        total += ((remaining_days * (remaining_days + 1)) // 2) + (week_count * remaining_days)
        
        return total
        
# Another way:
class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        money = w * 28
        money += (7 * w *( w - 1))//2

        if (n % 7):
            extra_days = n % 7
            money_to_add = w + 1
            for i in range(extra_days):
                money += money_to_add
                money_to_add += 1

        return money