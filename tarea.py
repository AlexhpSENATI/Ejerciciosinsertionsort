def tabla(arr):
    for i in range(1, len(arr)):
        j=i
        while j>0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1]= arr[j-1], arr[j],
            j-=1
    return arr
arr=[4,6,5,3]
xd= tabla(arr)
print(xd)