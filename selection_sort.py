def getBitCount(num: int) -> int:
    count = 0
    while True:
        if num % 2 == 1:
            count += 1
        num = num//2

        if num == 0:
            break
    return count

def getGroupDict(arr):
    group = {}
    for num in arr:
        bitCount = getBitCount(num)
        if bitCount in group:
            group[bitCount] += [num]
        else:
            group[bitCount] = [num]
    return group

def insertionSort(arr):
    for j in range(1,len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key

def sortGroupDict(group):
    for key in group:
        insertionSort(group[key])

def selectionSort(arr):
    for j in range(len(arr) - 1):
        min = j
        for i in range(j+1, len(arr)):
            if arr[i] < arr[min]:
                min = i
        arr[min], arr[j] = arr[j], arr[min]

# arr = [0,1,2,3,4,5,6,7,8]
arr = [6,3,567,9,3,2,46,7,3]
# group = getGroupDict(arr)
# sortGroupDict(group)
# print(group)

selectionSort(arr)
print(arr)