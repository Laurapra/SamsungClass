#quiz01
"""
La salida después de ejecutar las funciones sería:

[10, 12, 13, 15, 20, 22, 25]
"""
#programación en parejas
#quiz1
def kth_largest_element(arr, k):
    n = len(arr)
    if k > n:
        return None

    def partition(arr, l, r):
        pivot = arr[r]
        i = l - 1
        for j in range(l, r):
            if arr[j] >= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[r] = arr[r], arr[i+1]
        return i+1

    def quick_select(arr, l, r, k):
        if l == r:
            return arr[l]
        pivot_index = partition(arr, l, r)
        if k == n - pivot_index:
            return arr[pivot_index]
        elif k < n - pivot_index:
            return quick_select(arr, pivot_index+1, r, k)
        else:
            return quick_select(arr, l, pivot_index-1, k-(n-pivot_index))

    return quick_select(arr, 0, n-1, k-1)
