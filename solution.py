class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0

        diff = [1]
        length = len(s)
        substrings = []

        #for substring in substrings:
        for i in range(len(s)):
            l = 0
            for j in range(i,len(s)):
                if s[j] not in s[i:j]:
                    l += 1      

                    if j == len(s) - 1:
                        diff.append(l)

                else:
                    diff.append(l)
                    break
                                        
        return max(diff)
        
    
    def run(self,s):
        return self.lengthOfLongestSubstring(s)
        
        