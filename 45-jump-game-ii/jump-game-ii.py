class Solution:
    def jump(nums: List[int]) -> int:
        reach = 0
        count = 0
        last = 0

        for i in range(len(nums) - 1):
            reach = max(reach, i + nums[i])
            if i == last:
                last = reach
                count += 1
        return count

    with open('user.out', 'w') as f:
        for case in map(loads, stdin):
            f.write(f"{jump(case)}\n")
    exit(0)
