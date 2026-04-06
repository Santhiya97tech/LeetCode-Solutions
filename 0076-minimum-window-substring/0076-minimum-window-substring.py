class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter
        need=Counter(t)
        have ={}
        required=len(need)
        formed=0
        left=0
        min_len=float('inf')
        result=""
        for right in range(len(s)):
            char=s[right]
            have[char]=have.get(char,0)+1
            if char in need and have[char]==need[char]:
                formed+=1
            while formed==required:
                window=s[left:right+1]
                if len(window)<min_len:
                    min_len=len(window)
                    result=window
                have[s[left]]-=1
                if s[left] in need and have[s[left]]<need[s[left]]:
                    formed-=1
                left+=1
        return result        