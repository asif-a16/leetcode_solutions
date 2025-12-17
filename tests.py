from collections import defaultdict
frequencies = defaultdict(int)
nums = [1,2,2,3,3,3]
for num in nums:
    frequencies[num] += 1

print(frequencies.items())
sorted_freq = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
print(sorted_freq[0])