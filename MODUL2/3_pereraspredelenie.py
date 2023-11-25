# # my_list = input()
# # nums_str_cleaned = my_list.replace('[', '').replace(']', '').split(',')
# # nums = list(map(int, nums_str_cleaned))
# #
# # maximum = max(nums)
# # minimum = min(nums)
# # average_value = (min(nums) + max(nums)) / 2
# #
# # result = [x for x in nums if x > average_value]
# #
# # result += [x for x in nums if x <= average_value]
# #
# # print(result)
# # # print_result = []
# # # for elem in result:
# # #     if elem == result[0]:
# # #         print_result.append(f"[{elem}")
# # #     if elem == result[-1]:
# # #         print_result.append(f"{elem}]")
# # #         break
# # #     print_result.append(f"{elem}")
# # #
# # # print(print_result)
#
# nums = [1, 2, 3, 4, 5]
#
# # Calculate the average of the minimum and maximum values
# average_value = (min(nums) + max(nums)) / 2
#
# # Sort the list based on a custom key function
# # result = sorted(nums, key=lambda x: (x >= min(nums) and x < max(nums), x))
# result = [item for item in nums if item <= max(nums) and item >= min(nums)]
# print(result)
nums = [1, 2, 3, 4, 5]
print([num for num in nums if num > (min(nums) + max(nums) / 2)] +
      [num for num in nums if num <= (min(nums) + max(nums) / 2)])
