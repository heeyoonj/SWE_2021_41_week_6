from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

input_nums = input("Input: nums(ex. 2 7 11 15) = ")
input_target = input("target(ex. 9) = ")

nums = list(map(int, input_nums.split()))
target = int(input_target)

result = twoSum(nums, target)
print(f"Output: {result}")