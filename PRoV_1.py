def bubble_sort(arr):
    """
    performs sorting of a given list via bubble algorithm
    :param arr: list
    :return: sorted list
    """
    N = len(arr)
    for i in range(N-1):
        for j in range(N-i-1):
            if arr[j] > arr[j+1]:
                point = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = point
    return arr

