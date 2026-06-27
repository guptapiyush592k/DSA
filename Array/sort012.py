def sort012(arr):
    i = 0
    j = 0
    k = len(arr) - 1
    while(j<=k):
        if(arr[j] == 1):
            j += 1
        elif(arr[j] == 0):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j += 1
        elif(arr[j] == 2):
            temp = arr[k]
            arr[k] = arr[j]
            arr[j] = temp
            k -= 1
    return arr
    
print(sort012([2,0,1,2,2,2,1,0,0,2]))