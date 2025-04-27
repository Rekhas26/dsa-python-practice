def find_single_number(arr):
    dict_nums = {}
    single_nums = []
    for i in arr:
        if i in dict_nums:
            dict_nums[i] += 1
        else:
            dict_nums[i] = 1
    
    for ele in dict_nums:
        if dict_nums[ele] == 1:
            single_nums.append(ele)
    return single_nums

print(find_single_number([4,1,2,1,2,5]))

#XOR best solution with time comlexity
arr = [4,1,2,1,2]
result = 0
for num in arr:
    result ^= num
print(result)   # Output: 4
