class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # greedy approach based on end points
        
        # less than 1 intervals, no need to remove any intervals
        if len(intervals) <= 1:
            return 0
        
        # sort by end points
        intervals.sort(key=lambda x : x[1])
        
        count = 1  # 记录非交叉区间的个数
        end = intervals[0][1] # 记录区间分割点
        
        for i in intervals[1 : ]:
            if end <= i[0]: # end smaller than next start, not overlapping
                count += 1
                end = i[1]
        
        return len(intervals) - count        
    
# 代码随想录  总结如下难点： 
# 我来按照右边界排序，从左向右记录非交叉区间的个数。最后用区间总数减去非交叉区间的个数就是需要移除的区间个数了。
# 此时问题就是要求非交叉区间的最大个数。
# 右边界排序之后，局部最优：优先选右边界小的区间，所以从左向右遍历，留给下一个区间的空间大一些，从而尽量避免交叉。全局最优：选取最多的非交叉区间。
# 局部最优推出全局最优，试试贪心！
# 这里记录非交叉区间的个数还是有技巧的，如图：

# 难点一：一看题就有感觉需要排序，但究竟怎么排序，按左边界排还是右边界排。
# 难点二：排完序之后如何遍历，如果没有分析好遍历顺序，那么排序就没有意义了。
# 难点三：直接求重复的区间是复杂的，转而求最大非重复区间个数。
# 难点四：求最大非重复区间个数时，需要一个分割点来做标记。

# 作者：carlsun-2
# 链接：https://leetcode-cn.com/problems/non-overlapping-intervals/solution/435-wu-zhong-die-qu-jian-tan-xin-jing-di-qze0/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。