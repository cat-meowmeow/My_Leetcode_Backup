class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:return 0
        intervals.sort(key = lambda x:x[1]) #影响的是每一段的end值 而非start值
        n = len(intervals)
        end = intervals[0][1]     # end is first[]'s  end
        num = 1
        for i in intervals[1:]:   # i is current list[]   i from second[] begin:
            start = i[0]          # check each i's start value
            if start >= end:      # current start value > the former value
                num+=1
                end = i[1]       # update end,and then i will go next[]
        return (n-num)
