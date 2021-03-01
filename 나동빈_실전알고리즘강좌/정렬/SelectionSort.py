def selectionSort(Array):
    N = len(Array)
    for i in range(N):
        mini = 9999999999
        for j in range(i,N):
            if mini > Array[j]:
                mini = Array[j]
                index = j
        temp = Array[i]
        Array[i] = Array[index]
        Array[index] = temp
    return Array



if __name__ == "__main__":
    Array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(Array)
    print(selectionSort(Array))
