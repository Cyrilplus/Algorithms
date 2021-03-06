# -*- coding:utf-8 -*-

"""
希尔排序：
    插入排序的升级版，相隔为h的序列是有序的，然后不断缩小h。
知道h为1，这个最后一步就是插入操作。由于插入排序的性质，受输入
序列的顺序的影响。所以每一次插入排序都是在大部分是有序的序列上操
作的，所以速度很快。
"""

import numpy as np
import matplotlib.pyplot as plt


def shell_sorted(seq):
    count = len(seq)
    h = 1
    x = np.arange(count)
    rows = 1
    while h < count / 3:
        h = 3 * h + 1
        rows += 1
    fig, axes = plt.subplots(ncols=1, nrows=rows + 1)
    axes_tuple = axes.ravel()
    index = 0
    axes_tuple[index].bar(x, np.array(seq), 0.5)
    index += 1
    while h >= 1:
        # 插入排序，步进为h->1
        for i in range(h, count):
            for j in range(i, h - 1, -h):
                if seq[j] < seq[j - h]:
                    # swap
                    seq[j - h], seq[j] = seq[j], seq[j - h]
        axes_tuple[index].bar(x, np.array(seq), 0.5)
        index += 1
        h /= 3
    plt.show()


if __name__ == '__main__':
    array = np.random.randint(0, 200, (1, 100))[0]
    shell_sorted(list(array))
