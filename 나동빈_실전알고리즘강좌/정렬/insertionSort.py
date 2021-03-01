def insertionSort(Array):
    N = len(Array)
    for i in range(N-1):
        j = i
        while Array[j] > Array[j+1]:
            temp = Array[j]
            Array[j] = Array[j+1]
            Array[j+1] = temp
            j -= 1
    return Array

if __name__ == "__main__":
    Array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(Array)
    print(insertionSort(Array))
