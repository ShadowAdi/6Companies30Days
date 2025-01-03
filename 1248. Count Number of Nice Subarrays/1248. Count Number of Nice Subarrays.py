def count_subarrays(nums: list[int], k: int) -> int:
    n = len(nums)

    l, m = 0, 0
    res, odd = 0, 0

    for r in range(n):
        if nums[r] % 2:
            odd += 1
        while odd > k:
            if nums[l] % 2:
                odd -= 1
            l += 1
            m = l
        if odd == k:
            while not nums[m] % 2:
                m += 1
            res += (m - l) + 1
    return res


ans=count_subarrays([1,1,2,1,1],3)
print("Answer is: ",ans)