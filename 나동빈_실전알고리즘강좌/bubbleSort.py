def bubbleSort(Array):
    N = len(Array)
    for i in range(N):
        for j in range(i, N):
            if Array[j] < Array[i]:
                temp = Array[i]
                Array[i] = Array[j]
                Array[j] = temp
    return Array

if __name__ == "__main__":
    Array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(Array)
    print(bubbleSort(Array))
