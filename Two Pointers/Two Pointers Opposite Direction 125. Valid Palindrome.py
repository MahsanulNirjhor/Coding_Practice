class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        #print(l)
        #print(r)
        while l < r :
            if l < r and not self.alnum(s[l]):
                l += 1
            elif r > l and not self.alnum(s[r]):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                #print(f'l = {s[l]}     r = {s[r]}')
                    return False
                #else:
                l += 1
                r -= 1
            #print(f'l = {s[l]}     r = {s[r]}')
        return True
        
        
        
    def alnum(self, c):
        return (ord('A') <= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z') 
            or ord('0') <= ord(c) <= ord('9'))



    """
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            l,r = 0, len(s) - 1
            
            while l < r :
                if not s[l].isalnum():
                    l += 1
                elif not s[r].isalnum():
                    r -= 1
                else: 
                    if s[l].lower() != s[r].lower():
                        print(f's[l] = {s[l]}  s[r] = {s[r]}')
                        return False
                    l+=1
                    r-=1
            return True
        
    """
        