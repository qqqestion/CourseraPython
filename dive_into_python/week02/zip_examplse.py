nums = list(map(int, input().split()))
square_list = [nums[i] for i in range(len(nums)) if nums[i] % 2 == 0]
print(list(zip(nums, square_list)))
