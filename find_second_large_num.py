def second_large_num(nums):
    if len(nums) < 2:
        return print("more then two number required")
    
    first, second = float('-inf'), float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    return second if second != float('-inf') else None


nums = [1,2,3,4,5,6,7,8,10]
print(second_large_num(nums))