arr1 = [4,6,2,1,9,63,-134,566]
def minimum(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

def maximum(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num
print("min:", minimum(arr1)) # -134
print("max:", maximum(arr1)) # 566
