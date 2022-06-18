import random
dataList = ["Alice","Jones","Billy Bob","Steve","david","Alex","foo","foobar","bar"] 
#The initial list isn't sorted, so when we get our result, we may be confused as to why it's not in the correct index. 
#Presumably you would have another list containing the sorted data list, and then you can get it at the correct index.
#And remember, Binary Search Algorithms rely on SORTED lists. If it were unsorted, it would be quite confused.
Rtarget = random.randint(0,len(dataList) - 1)
target = dataList[Rtarget]
def BinarySearch(targ,min,max,array):
    dataList.sort()
    count = 0
    while True:
        middle = min + (max - min)//2
        if array[middle] == targ:
            print(array[middle])
            print(f"targ is at index {middle} of list")
            return(count)
        elif array[middle] < targ:
            min = middle + 1
        elif array[middle] > targ:
            max = middle - 1
        count += 1
c = BinarySearch(target,1,len(dataList)-1,dataList)
print("Count:{}".format(c))