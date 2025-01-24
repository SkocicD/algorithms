def sort(arr):
    if len(arr) > 1:
        index = len(arr) // 2
        left = sort(arr[:index])
        right = sort(arr[index:])
        return merge(left, right)
    else:
        return arr

def merge(left, right):
    ret = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index]['l'] > right[right_index]['l']:
            ret.append(right[right_index])
            right_index += 1
        else:
            ret.append(left[left_index])
            left_index += 1
    while left_index < len(left):
        ret.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        ret.append(right[right_index])
        right_index += 1

    return ret
