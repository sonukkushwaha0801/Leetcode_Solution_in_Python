# Visit the profile for more solutions with minimum complexity
# https://leetcode.com/sonukkushwaha0801/
# type first:

from typing import List


class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        robots.sort()
        factories.sort()
        factory_positions = []
        for factory in factories:
            for i in range(factory[1]):
                factory_positions.append(factory[0])

        robot_count = len(robots)
        factory_count = len(factory_positions)
        next_dist = [0 for _ in range(factory_count + 1)]
        current = [0 for _ in range(factory_count + 1)]
        for i in range(robot_count - 1, -1, -1):
            if i != robot_count - 1:
                next_dist[factory_count] = 1e12
            current[factory_count] = 1e12

            for j in range(factory_count - 1, -1, -1):
                assign = (abs(robots[i] - factory_positions[j]) + next_dist[j + 1])
                skip = current[j + 1]
                current[j] = min(assign, skip)
            next_dist = current[:]
        return current[0]
    
# Another way:

from typing import List

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])
        
        memo = {}

        def helper(currRobot, currFact, usedCapacity):
            if currRobot == len(robot):
                return 0
            if currFact == len(factory):
                return float('inf')

            key = (currRobot, currFact, usedCapacity)
            if key in memo:
                return memo[key]

            # Option 1: Skip to the next factory
            minDist = helper(currRobot, currFact + 1, 0)

            # Option 2: Use current factory if capacity allows
            position, capacity = factory[currFact]
            if usedCapacity < capacity:
                dist = abs(robot[currRobot] - position)
                minDist = min(minDist, dist + helper(currRobot + 1, currFact, usedCapacity + 1))

            memo[key] = minDist
            return minDist

        return helper(0, 0, 0)
        