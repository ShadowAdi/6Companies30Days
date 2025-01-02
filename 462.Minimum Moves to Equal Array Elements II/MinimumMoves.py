def MinimumMovesBrute(nums: list[int]) -> int:

    nums.sort()
    steps = 0
    n = len(nums)

    median = nums[n // 2]

    for i in nums:
        steps += abs(median - i)
    return steps


def MinimumMoves(nums: list[int]) -> int:

    nums.sort()
    steps = 0
    n = len(nums)

    i, j = 0, n - 1

    while i < j:
        steps += nums[j] - nums[i]
        i += 1
        j -= 1
    return steps


ans = MinimumMoves([1, 10, 2, 9])
print(ans)
