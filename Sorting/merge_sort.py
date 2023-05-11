'''
Merge Sort Code in Python
'''

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        leftArray = arr[:mid]
        rightArray = arr[mid:]

        mergeSort(leftArray)
        mergeSort(rightArray)

        leftIndex = rightIndex = mergeIndex = 0
 
        while leftIndex < len(leftArray) and rightArray < len(rightArray):
            if leftArray[leftIndex] <= rightArray[rightIndex]:
                arr[mergeIndex] = leftArray[leftIndex]
                leftIndex += 1
            else:
                arr[mergeIndex] = rightArray[rightIndex]
                rightIndex += 1
            mergeIndex += 1
 
        while leftIndex < len(leftArray):
            arr[mergeIndex] = leftArray[leftIndex]
            leftIndex += 1
            mergeIndex += 1
 
        while rightIndex < len(rightArray):
            arr[mergeIndex] = rightArray[rightIndex]
            rightIndex += 1
            mergeIndex += 1


arr = [12, 11, 13, 5, 6, 7]
print(arr)
mergeSort(arr)  #0, 5
print(arr)