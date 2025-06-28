nums = [int(ch) for ch in input() if ch != '0']
while len(nums) > 1:
    prod = 1
    for num in nums:
        prod *= num
    nums = [int(ch) for ch in str(prod) if ch != '0']
print(nums[0])
