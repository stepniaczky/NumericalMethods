
def horner(arr, x):
    result = arr[0]
    for i in range(1, len(arr)):
        result *= x + arr[i]
    return result
