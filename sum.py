def reverseArray(self, arr):
    i = 0
    while (i < len(arr)/2):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1 - i]
        arr[len(arr) - 1 - i] = temp
        i += 1
            
    return arr