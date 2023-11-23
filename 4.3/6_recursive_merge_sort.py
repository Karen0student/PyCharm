def merge_sort(my_list):
    def merge(left, right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    if len(my_list) <= 1:
        return my_list

    mid = len(my_list) // 2
    left_half = merge_sort(my_list[:mid])
    right_half = merge_sort(my_list[mid:])

    return merge(left_half, right_half)


print(merge_sort([3, 2, 1]))
