def wiggleSort(nums: list[int]) -> None:
    nums.sort()
    n = len(nums)
    mid = (n + 1) // 2

    smaller = nums[:mid][::-1]
    larger = nums[mid:][::-1]
    nums[::2], nums[1::2] = smaller, larger
    print("Array is: ",nums)

wiggleSort([1,5,1,1,6,4])
