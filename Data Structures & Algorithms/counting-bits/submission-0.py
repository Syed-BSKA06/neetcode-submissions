class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones(num):
            count = 0
            while num:
                num = num & (num-1)
                count +=1 
            return count
        result = []
        for i in range(n+1):
            result.append(count_ones(i))
        return result
        