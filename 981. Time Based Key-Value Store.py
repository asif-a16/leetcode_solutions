from collections import defaultdict
import bisect

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        bisect.insort(self.map[key], (timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        bucket = self.map[key]
        if not bucket:
            return ""
        left = 0
        right = len(bucket) - 1
        while left <= right:
            pivot = left + int((right - left) / 2)
            if bucket[pivot][0] == timestamp:
                return bucket[pivot][1]
            elif timestamp < bucket[pivot][0]:
                right = pivot - 1
            else:
                left = pivot + 1
        min_idx = min(left, right)
        return bucket[min_idx][1] if bucket[min_idx][0] <= timestamp else ""
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)