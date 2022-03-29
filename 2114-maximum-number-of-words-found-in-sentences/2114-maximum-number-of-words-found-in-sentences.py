class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(" ") for s in sentences) + 1
        
        # return max(len(s.split()) for s in sentences)
        
#         most = 0 
#         for s in sentences:
#             most = max(most, len(s.split()))
#         return most