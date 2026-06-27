def rotate( arr):
        i = 0
        j = len(arr) - 1
        while(i <= j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
        print(arr)

rotate([1,2,3,4,5,6,7,8,9])