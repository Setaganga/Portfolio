import random
numbers = []
for _ in range(int(input("Enter max number for program:")) + 1):
    numbers.append(_)
Rtarget = random.randint(numbers[0],numbers[-1])
target = numbers[Rtarget]
def BinarySearch(targ,min,max,array):
    count = 0
    while True:
        middle = min + (max - min)//2
        if array[middle] == targ:
            print(array[middle])
            return(count)
        elif array[middle] < targ:
            min = middle + 1
        elif array[middle] > targ:
            max = middle - 1
        count += 1
c = BinarySearch(target,1,len(numbers)-1,numbers)
print("Count:{}".format(c))
