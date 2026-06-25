def getMinMax(self, arr):
        min = arr[0]
        max = arr[0]
        
        for i in range(len(arr)):
            if(arr[i] > max):
                max = arr[i]
            elif(arr[i] < min):
                min = arr[i]
                
        return [min, max]