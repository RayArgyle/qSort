# coding=utf-8
import random

data = [random.randint(0, 10) for i in range(0, 10)]

def partition(array, start, end):
    pivot = array[(start+end) // 2]
    i=start
    j=end

    while i <=j:
        while array[i] < pivot:
            i+=1
        while array[j] > pivot:
            j-=1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i+=1
            j-=1
    return i

def qsort(array, start, end):
    if start < end:
        temp = partition(array, start, end)
        qsort(array, start, temp -1)
        qsort(array, temp, end)

print(data)
qsort(data, 0, len(data)-1)
print(data)
