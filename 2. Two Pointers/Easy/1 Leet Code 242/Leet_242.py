from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #------------Solution 1---------------------------
        if len(s) != len(t):
            return False
        counter_s, counter_t = {}, {}

        for i in range(len(s)):
            counter_s[s[i]] = 1 + counter_s.get(s[i],0)
            #print(counter_s)
            counter_t[t[i]] = 1 + counter_t.get(t[i],0)
            #print(counter_t)

        for c in counter_s:
            if counter_s[c] != counter_t.get(c,0):
                return False
        return True
        #------------Solution 2 ---------------------------
        if Counter(s) == Counter(t):
            return True
        #------------Solution 3 ---------------------------
        if sorted(s) == sorted(t):
            return True 
        