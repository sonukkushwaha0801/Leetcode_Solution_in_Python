# Visit the profile for more solutions with minimum complexity
#https://leetcode.com/sonukkushwaha0801/
# type first :
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        for i in range(1, len(arr)):
            arr[i] ^= arr[i - 1]
        
  
        return [arr[end] ^ arr[start - 1] if start > 0 else arr[end] 
                for start, end in queries]

def kdsmain():
    input_data = sys.stdin.read().strip()
    lines = input_data.splitlines()
    
    num_test_cases = len(lines) // 2
    results = []

    for i in range(num_test_cases):
        arr = json.loads(lines[i*2])
        queries = json.loads(lines[i*2 + 1])
        
        result = Solution().xorQueries(arr, queries)
        results.append(json.dumps(result, separators=(',', ':')))

    with open('user.out', 'w') as f:
        for result in results:
            f.write(f"{result}\n")

if __name__ == "__main__":
    kdsmain()
    exit(0)

# Another way:
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Step 1: Create a prefix XOR array
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        
        # Fill the prefix_xor array
        for i in range(1, n + 1):
            prefix_xor[i] = prefix_xor[i - 1] ^ arr[i - 1]
        
        # Step 2: Answer each query
        result = []
        for left, right in queries:
            result.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return result