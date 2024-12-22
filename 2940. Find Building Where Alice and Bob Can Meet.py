# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# Type one:

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        N = len(heights)
        bucket_size = int((N ** 0.5))
        max_heights_per_bucket = []
        current_max_height = float('-inf')
        current_bucket_size = 0
        i = 0
        while i < N:
            current_max_height = max(current_max_height, heights[i])
            current_bucket_size += 1
            if current_bucket_size == bucket_size:
                max_heights_per_bucket.append(current_max_height)
                current_max_height = float('-inf')
                current_bucket_size = 0
            i += 1
        if current_max_height != float('-inf'):
            max_heights_per_bucket.append(current_max_height)

        result = []
        for query in queries:
            left, right = sorted(query)
            if left == right or heights[right] > heights[left]:
                result.append(right)
                continue
            needed_height = max(heights[left], heights[right]) + 1
            right_bucket = right // bucket_size
            for i in range(right, min(N, (right_bucket + 1) * bucket_size)):
                if heights[i] >= needed_height:
                    result.append(i)
                    break
            else:
                for bucket_idx in range(right_bucket + 1, len(max_heights_per_bucket)):
                    if max_heights_per_bucket[bucket_idx] >= needed_height:
                        target_bucket_idx = bucket_idx
                        break
                else:
                    result.append(-1)
                    continue
                for i in range(target_bucket_idx * bucket_size, min(N, (target_bucket_idx + 1) * bucket_size)):
                    if heights[i] >= needed_height:
                        result.append(i)
                        break
        return result