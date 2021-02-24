def QuickSort(Array):
    if len(Array)<=1:
        return Array
    pivot = Array[len(Array)//2]
    less_pivot, over_pivot = [], []
    for num in Array:
        if num > pivot:
            over_pivot.append(num)
        elif num < pivot:
            less_pivot.append(num)
    return QuickSort(less_pivot)+[pivot]+QuickSort(over_pivot)

if __name__ == "__main__":
    Array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
    print(Array)
    print(QuickSort(Array))