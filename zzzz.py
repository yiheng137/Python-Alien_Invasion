import math
# page_num starts from 0 or 1?
def pagination(arr, page_num, page_size):  # page num starts from 1
    """Simple pagination method"""
    p = (page_num - 1) * page_size
    return arr[p:p + page_size]


def pagination2(arr, start, page_num, page_size):  # 'start' starts from 0; 'page_num' starts from 1
    """Simple circularized pagination with a start position"""
    # step 1 reorder the arr
    arr = arr[start:] + arr[: start]

    # do pagination
    p = (page_num - 1) * page_size
    return arr[p:p + page_size]


def pagination3(arr, start, page_num, page_size):  # 'start' starts from 0; 'page_num' starts from 1
    """Circularized pagination with a start position. Do not reorder the arr"""
    size = len(arr)
    max_page_num = math.ceil(size / page_size)
    if page_num > max_page_num:  # when the specified page_num exceeds the largest page_num of the array, return []
        return []

    l = (start + (page_num - 1) * page_size) % size  # compute the left position of the required sub-array
    r = l + page_size  # the right position of the required sub-array (excluded)

    if r >= size:  # hit the end of the array
        return arr[l:] + arr[:min(r % size, start)]  # in case the page exceed the start point
    else:
        return arr[l:r]


arr = [i for i in range(10)]

print(arr)
# print(pagination2(arr, 3, 1, 4))
print(pagination3(arr, 3, 2, 6))
