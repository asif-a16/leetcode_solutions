import bisect

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        bisect.insort(intervals, newInterval)
        if not intervals:
            return intervals
        
        result = []
        cur_interval = intervals[0]

        def overlapsWith(interval1: list[int], interval2: list[int]) -> bool:
            if ((interval1[1] >= interval2[0] and interval2[0] >= interval1[0]) or 
                (interval1[0] <= interval1[1] and interval1[1] >= interval2[0])):
                return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]
            return False

        for interval in intervals:
            merged_interval = overlapsWith(cur_interval, interval)

            if not merged_interval:
                result.append(cur_interval)
                cur_interval = interval
            else:
                cur_interval = merged_interval

        result.append(cur_interval)
        return result
