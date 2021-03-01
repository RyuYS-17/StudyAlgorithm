def HeapSort(Array):
    N = len(Array)
    for i in range(1, N):
        idx = i
        while(idx != 0):
            root = (idx-1)//2
            if Array[idx] > Array[root]:
                temp = Array[idx]
                Array[idx] = Array[root]
                Array[root] = temp
            idx = root
    for i in range(N-1,-1,-1):
        temp = Array[0]
        Array[0] = Array[i]
        Array[i] = temp

        root = 0
        child = 1
        while (child<i):
            if (Array[child] < Array[child+1] and child < i-1):
                child += 1
            if (Array[root] < Array[child] and child<i):
                temp = Array[root]
                Array[root] = Array[child]
                Array[child] = temp
            root = child
            child = root*2+1            
    return Array

if __name__ == "__main__":
    import random
    Array = []
    for _ in range(random.randint(5,15)):
        Array.append(random.randint(0,10))
    print(Array)
    print(HeapSort(Array))
