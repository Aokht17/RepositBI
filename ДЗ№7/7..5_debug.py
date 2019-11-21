def binary_search(arr1, x, l=0, r=None):
    """
    Returns the number of the element using binary search
    :param arr: massive
    :param l: the start element (default = 0)
    :param r: the end of the cycle, (default (len(arr)-1)
    :param x: element
    """
    arr = sorted(arr1)
    r = (len(arr)-1) if r is None else r

    if r >= l:

        half = int(l + (r - l) / 2)

        if arr[half] == x:
            return half

        elif arr[half] > x:  # elements can be present in left subarray
            return binary_search(arr, x, l, half-1)

        else:  # or in right subarray
            return binary_search (arr, x, half + 1, r)

    else:
        return None



arr5 = [2, 3, 4, 10, 40]
x = 10
print(binary_search(arr1=arr5, x=x))

arr3 ='frhyarcdye'
print(binary_search(arr3,'d'))
