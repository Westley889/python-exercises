import sys
def filter_sort(arnade):
    array = []
    for nums in arnade:
        if nums not in array:
            array.append(nums)
    return sorted(array)

num = []
for nums in sys.argv:
    num.append(nums)
num.remove(num[0])

print("%s" % filter_sort(num))