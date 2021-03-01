def mergeSort(Array):
    if len(Array)<2:
        return Array
    middle = len(Array)//2
    lowArray = mergeSort(Array[:middle])
    highArray = mergeSort(Array[middle:])

    mergeArray = []
    i = j = 0
    while (i < len(lowArray) and j < len(highArray)):
        if lowArray[i] < highArray[j]:
            mergeArray.append(lowArray[i])
            i += 1
        else:
            mergeArray.append(highArray[j])
            j += 1
    mergeArray += lowArray[i:]
    mergeArray += highArray[j:]

    return mergeArray

if __name__ == "__main__":
    import random
    size = random.randint(5, 30)
    Array = []
    for _ in range(size):
        Array.append(random.randint(1,1000))
    print(Array)
    print(mergeSort(Array))
