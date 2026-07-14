class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        need_count = len(need)
        have = 0
        left = 0
        window = {}
        result , result_len = "", float('inf')

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0) + 1

            if char in need and window[char] == need[char]:
                have+=1
            while have == need_count:
                if(right-left+1) < result_len:
                    result_len = right-left+1
                    result = s[left:right+1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char]<need[left_char]:
                    have-=1

                left+=1

        return result


        