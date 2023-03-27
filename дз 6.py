from random import randint


def sel_sort(array):
    for i in range(len(array) - 1):
        m = i
        j = i + 1
        while j < len(array):
            if array[j] < array[m]:
                m = j
            j = j + 1
        array[i], array[m] = array[m], array[i]


a = []
for i in range(10):
    a.append(randint(1, 99))

print(a)
sel_sort(a)
print(a)

from random import randint

a = []
for i in range(10):
    a.append(randint(1, 50))
a.sort()
print(a)

value = int(input())

mid = len(a) // 2
low = 0

while a[mid] != value and low <= high:
    if value > a[mid]:
        low = mid + 1
    else:
        high = mid - 1
    mid = (low + high) // 2

if low > high:
    print("No value")
else:
    print("ID =", mid)
    def binary_searh(lst, search_item):
        low=0;
        high=len(lst)-1
        searc_res=False
        while low <=high and not searc_res:
            middle = (low + high) // 2
            qess = lst[middle]
            if qess==search_item:
                searc_res=True
                return  searc_res
            if qess>search_item:
                high = middle - 1
            else:
                low = middle + 1
                return searc_res
            lst = [3, 5, 11, 12, 15, 23, 25, 34, 67,86]
            value=91
            results= binary_searh(lst,value)
            if results:
                print("Элемент найден")
            else:
                print("Элемент не найден")