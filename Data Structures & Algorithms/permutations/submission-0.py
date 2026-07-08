class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(current, visited):
            if len(current) == len(nums):
                result.append(current[:])
                return 
            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                current.append(nums[i])
                backtrack(current,visited)
                current.pop()
                visited.remove(i)
        backtrack([], set())
        return result
                
                
        