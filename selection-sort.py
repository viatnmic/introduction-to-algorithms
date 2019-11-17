def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp

def indexOfMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex

    for i in xrange(minIndex + 1, len(array)):
        if minValue > array[i]:
            minIndex = i
            minValue = array[i]
    
    return minIndex

def selectionSort(array):
    for i in range(len(array)):
        # find the index of the minimum value in subarray
        minIndex = indexOfMinimum(array, i)
        # swap location of minimum value in array to the current location
        swap(array, minIndex, i)