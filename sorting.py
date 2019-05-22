# 1. selection sort
# 2. insertion sort
# 3. shell sort
# 4. heap sort
# 5. merge sort
# 6. quick sort

import time
import random
import matplotlib.pyplot as plt

class Sorting(object):
    """Sorting class

    """

    def __init__(self):
        self.id = []

    def sort_init(self, N):
        """initialize the data structure

        """

        try:
            self.id = random.sample(range(1, N ** 3), N)
        except ValueError:
            print('Sample size exceeded population size.')

        # self.id = [random.randint(0, N - 1) for i in range(N)]

    def get_id(self):
        """initialize the data structure

        """

        return self.id

#swap function
    def swap(self, i, j):
        temp = self.id[i]
        self.id[i] = self.id[j]
        self.id[j] = temp

    def selection_sort(self):
        """Selection sort algorithm is an
        in-place comparison sort. It has O(n^2) time complexity, making it
        inefficient on large lists, and generally performs worse than the
        similar insertion sort

        """
        for i_idx, i_item in enumerate(self.id):
            min = i_idx

            for j_idx in range(i_idx+1, len(self.id)): #starting index, length

                if (self.id[j_idx] < self.id[min]):
                    min = j_idx

            self.swap(min, i_idx)
            # swap
            # temp = self.id[i_idx]
            # self.id[i_idx] = self.id[min]
            # self.id[min] = temp

        return self.id


    def insertion_sort(self):
        """Insertion sort is a simple sorting algorithm that builds the final
        sorted array (or list) one item at a time. More efficient in practice
        than most other simple quadratic (i.e., O(n^2)) algorithms such as
        selection sort or bubble sort specifically an

        """
        for i in range(1, len(self.id)):
            key = self.id[i]
            j = i
            while j > 0 and self.id[j-1] > key:
                self.id[j] = self.id[j-1]
                j -= 1
            self.id[j] = key

        return self.id


    def shell_sort(self):
        """Shell sort also known as  or Shell's method, is an in-place comparison sort.
        It can be seen as either a generalization of sorting by exchange (bubble sort)
        or sorting by insertion (insertion sort).

        """
        n = len(self.id)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.id[i]
                j = i
                while j >= gap and self.id[j - gap] > temp:
                    self.id[j] = self.id[j - gap]
                    j -= gap
                    self.id[j] = temp
            gap //= 2
        return self.id


    def heapify(self, arr, n, i):
        large = i #index of largest number
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[l] > arr[large]:
            large = l
        if r < n and arr[r] > arr[large]:
            large = r
        if large != i:
            arr[large], arr[i] = arr[i], arr[large]
            self.heapify(arr, n, large)

    def build_heap(self, arr):
        n = len(arr)
        k = n//2 - 1
        for i in range(k, -1, -1):
            self.heapify(arr, n, i)
        for j in range(n - 1, -1, -1):
            arr[j], arr[0] = arr[0], arr[j]
            self.heapify(arr, j, 0)

    def heap_sort(self):
        """Heapsort is an improved selection sort: it div   ides its input into a sorted
        and an unsorted region, and it iteratively shrinks the unsorted region by
        extracting the largest element and moving that to the sorted region.

        """
        self.build_heap(self.id)
        return self.id

    def merge(self, list):
        n = len(list)
        if n > 1:
            mid = n // 2
            left = list[:mid]
            right = list[mid:]

            self.merge(left)
            self.merge(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i = i + 1
                else:
                    list[k] = right[j]
                    j = j + 1
                k = k + 1
            while i < len(left):
                list[k] = left[i]
                i = i + 1
                k = k + 1
            while j < len(right):
                list[k] = right[j]
                j = j + 1
                k = k + 1

    def merge_sort(self):
        """Merge sort is a divide and conquer algorithm that was invented
        by John von Neumann in 1945. Most implementations produce a stable
        sort, which means that the implementation preserves the input order
        of equal elements in the sorted output.
        """
        self.merge(self.id)


        return self.id

    #partition
    def partition(self, list, low, high):
        i = (low - 1)
        pind = list[high]

        for j in range(low, high):
            if list[j] <= pind:
                i = i + 1
                list[i], list[j] = list[j], list[i]

        list[i + 1], list[high] = list[high], list[i + 1]

        return i + 1

    def quick(self, arr, lo, hi):
        if lo < hi:
            ind = self.partition(arr, lo, hi)
            self.quick(arr, lo, ind - 1)
            self.quick(arr, ind + 1, hi)
        # return self.id

    def quick_sort(self):
        """Quicksort (sometimes called partition-exchange sort) is an efficient
        sorting algorithm. Developed by Tony Hoare in 1959. It is still a commonly
        used algorithm for sorting. When implemented well, it can be about two or
        three times faster than its main competitors, merge sort and heapsort.

        """
        self.quick(self.id, 0, len(self.id)-1)
        return self.id


if __name__ == "__main__":

    for i in range(0, 5):
        set_szs = [10, 100, 1000, 10000]
        timing = []
        for set_sz in set_szs:
            inodes = Sorting()
            inodes.sort_init(set_sz)
            t0 = time.time()

            if i == 0:
                inodes.selection_sort()
            elif i == 1:
                inodes.insertion_sort()
            elif i == 2:
                inodes.shell_sort()
            elif i == 3:
                inodes.heap_sort()
            elif i == 4:
                inodes.merge_sort()
            elif i == 5:
                inodes.quick_sort()
            else:
                pass

            t1 = time.time()
            total_time = t1 - t0
            timing.append(total_time)
            print(total_time)

        if i == 0:
            print("selection_sort:")
            plt.plot(set_szs, timing, label='selection_sort')
        elif i == 1:
            print("insertion_sort:")
            plt.plot(set_szs, timing, label='insertion_sort')
        elif i == 2:
            print("shell_sort:")
            plt.plot(set_szs, timing, label='shell_sort')
        elif i == 3:
            print("heap_sort:")
            plt.plot(set_szs, timing, label='heap_sort')
        elif i == 4:
            print("merge_sort:")
            plt.plot(set_szs, timing, label='merge_sort')
        elif i == 5:
            print("quick_sort")
            plt.plot(set_szs, timing, label='quick_sort')
        else:
            pass

    plt.xscale('log')
    plt.yscale('log')
    plt.title('Sorting')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.legend()
    plt.show()