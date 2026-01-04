class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # partitions_from[i] = all palindrome partitions of s[i:]
        partitions_from = [[] for _ in range(len(s) + 1)]
        partitions_from[len(s)] = [[]]  # base case: one way to partition empty suffix

        for start in range(len(s) - 1, -1, -1):
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                if substring == substring[::-1]:  # check palindrome
                    for suffix_partition in partitions_from[end]:
                        partition = [substring] + suffix_partition
                        partitions_from[start].append(partition)

        return partitions_from[0]
