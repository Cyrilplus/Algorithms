# -*- coding:utf-8 -*-

"""
归并排序:
    将两个有序的序列合并成一个有序的序列
"""

import math


def merge(array1, array2, compare=cmp):
    count1 = len(array1)
    count2 = len(array2)
    i, j = 0, 0
    array = []
    for count in range(0, count1 + count2):
        if i >= count1:
            array.append(array2[j])
            j += 1
        elif j >= count2:
            array.append(array1[i])
            i += 1
        elif compare(array1[i], array2[j]) < 0:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1
    return array


g_array = []    # global variable


def merge_sorted(array, compare=cmp):
    count = len(array)
    mid = int(math.ceil(count / 2.0))
    global g_array
    if count == 1:
        return
    left = array[0:mid]
    right = array[mid:count]
    merge_sorted(left, compare)
    merge_sorted(right, compare)
    print "sortedArray:" + str(g_array)
    print "left" + str(left)
    print 'right:' + str(right)
    g_array = merge(g_array, left)
    g_array = merge(g_array, right)


if __name__ == '__main__':
    '''
    array1 = [1, 2, 3, 9, 10]
    array2 = [4, 5, 6, 12]
    array = merge(array1, array2)
    print array
    '''
    array3 = [10, 11, 12, 3, 2, 1]
    merge_sorted(array3)
    # print sortedArray
