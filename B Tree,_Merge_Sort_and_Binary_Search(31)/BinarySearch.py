
# implimented to find duplicates
def searchDu(arr, mid):
    narr = [arr[mid]]
    i = 1
    try:
        while arr[mid][0] == arr[mid+i][0]:
            narr.append(arr[mid+i])
            i += 1
    except Exception:
        pass
    try:
        while arr[mid][0] == arr[mid-i][0]:
            narr.append(arr[mid-i])
            i += 1
    except Exception:
        pass
    return narr


def binarySearch(arr, l, r, x):

    # Check base case

    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if arr[mid][0] == x:
            return searchDu(arr, mid)

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid][0] > x:
            return binarySearch(arr, l, mid-1, x)

        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)

    else:
        # Element is not present in the array
        return (0, "Not Found")


# Driver Code
# arr = [(66, 'Gayashan'), (66, 'Rukshan'), (77, 'Heshan'), (88, "Keshan")]
# x = 66
# index = []
# # # Function call
# print(binarySearch(arr, 0, len(arr)-1, x))
