def highestOccurring(nums):
    max_count = 0
    ans = nums[0]

    for i in nums:
        count = nums.count(i)

        if count > max_count or (count == max_count and i < ans):
            max_count = count
            ans = i

    return ans