class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res =""
        for i in range(n):
            res += word1[i] + word2[i]
        return res + word1[n:] + word2[n:]
        
        # return "".join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
                
#         res = ""
#         l1, l2 = len(word1), len(word2)
#         minl = min(l1, l2)

#         for i in range(minl):
#             res += word1[i] + word2[i]
        
#         if l1 < l2:
#             res += word2[minl:]
#         elif l1 > l2:
#             res += word1[minl:]
#         return res