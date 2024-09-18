
# def ejemplo(array):
#     for i in range(1, len(array)):
#         key = array[i] 
#         j = i - 1
#         while j >= 0 and key < array[j]:
#             array[j + 1] = array[j]
#             j -= 1       
#         array[j + 1] = key
#     return array
# array = [20,15,18,12, 11, 13, 5, 6]
# xd1 = ejemplo(array)
# print(xd1)
def ejemplo(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Intercambia los elementos
            j -= 1
    return arr

arr = [12, 11, 13, 5, 6]
xd1 = ejemplo(arr)
print(xd1)

