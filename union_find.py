# 1. quick-find
# 2. quick-union
# 3. weighted QU
# 4. QU + path compression
# 5. weighted QU + path compression

import time
import random
import matplotlib.pyplot as plt

class UF(object):
    def __init__(self):
        """ declaring array """
        self.id = []
        self.sz = []


    def qf_init(self, N):
        """ Initializing array """

        for x in range(N):
            self.id.append(x)
        for y in range(N):
            self.sz.append(1)


    def qf_union(self, p, q):
            temp = self.id[p]
            for i in range(len(self.id)):
                if self.id[i] == temp:
                    self.id[i] = self.id[q]
            return 1



    def qf_connected(self, p, q):
        if self.id[p] == self.id[q]:
            return True
        else:
            return False

    def qu_union(self, p, q):

        while p != self.id[p]:
            p = self.id[p]

        while q != self.id[q]:
            q = self.id[q]

        self.id[p] = q
        return 1


    def qu_connected(self, p, q):

        while p != self.id[p]:
             p = self.id[p]

        while q != self.id[q]:
            q = self.id[q]
        return q == p




    def wqu_union(self, p, q):

        while p != self.id[p]:
             p = self.id[p]
        i = p
        while q != self.id[q]:
            q = self.id[q]
        j = q
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
                self.id[i] = j
                self.sz[j] += self.sz[i]
        else:
               self.id[j] = i
               self.sz[i] += self.sz[j]
        return 1

    def wqu_connected(self, p, q):
        """Find operation for Weighted Quick-Union Algorithm.
         test whether p and q are connected

         """
        while p != self.id[p]:
            p = self.id[p]
        i = p
        while q != self.id[q]:
            q = self.id[q]
        j = q
        return i == j

    def pqu_union(self, p, q):
        """Union operation for path compressed Quick-Union Algorithm.
         connect p and q.

         """
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]

        while q != self.id[q]:
            self.id[q] = self.id[self.id[q]]
            q = self.id[q]

        self.id[p] = q
        return 1


    def pqu_connected(self, p, q):
        """Find operation for path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]

        while q != self.id[q]:
            self.id[q] = self.id[self.id[q]]
            q = self.id[q]

        return p == q


    def wpqu_union(self, p, q):
        """Union operation for Weighted path compressed Quick-Union Algorithm.
         connect p and q.

         """
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        i = p
        while q != self.id[q]:
            self.id[q] = self.id[self.id[q]]
            q = self.id[q]
        j = q
        if i == j:
            return
        if self.sz[i] < self.sz[j]:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
        return 1


    def wpqu_connected(self, p, q):
        """Find operation for Weighted path compressed Quick-Union Algorithm.
         test whether p and q are connected

         """
        while p != self.id[p]:
            self.id[p] = self.id[self.id[p]]
            p = self.id[p]
        i = p
        while q != self.id[q]:
            self.id[q] = self.id[self.id[q]]
            q = self.id[q]
        j = q
        return i == j

if __name__ == "__main__":

    # iteration
    set_szs = [10, 100, 1000, 10000]
    timing = []

    print("qf_union:\n")
    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.qf_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!
    plt.plot(set_szs, timing,label='qf_union')

##############2
    # iteration
    set_szs =  [10, 100, 1000, 10000]
    timing = []
    print("qu_union:\n")
    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

        inodes.qu_union(rp, rq)

        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!
    plt.plot(set_szs, timing,label='qu_union')

    ############3
    # iteration
    set_szs =  [10, 100, 1000, 10000, 100000]
    timing = []

    print("wqu_union:\n")
    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)


            inodes.wqu_union(rp, rq)


        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!

    plt.plot(set_szs, timing,label='wqu_union')

    ##############3
    # iteration
    set_szs =  [10, 100, 1000, 10000, 100000]
    timing = []

    print("pqu_union:\n")
    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)

            inodes.pqu_union(rp, rq)


        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!
    plt.plot(set_szs, timing,label='pqu_union')

    ####################4
    # iteration
    set_szs = [10, 100, 1000, 10000, 100000]
    timing = []
    print("wpqu_union:\n")

    # gives the timing for union operation only, you might want to do this for all functions you wrote.
    for set_sz in set_szs:
        # initialize network nodes
        inodes = UF()
        inodes.qf_init(set_sz)

        t0 = time.time()

        for idx in range(set_sz - 1):
            rp = random.randint(0, set_sz - 1)
            rq = random.randint(0, set_sz - 1)


            inodes.wpqu_union(rp, rq)


        t1 = time.time()

        total_time = t1 - t0

        timing.append(total_time)

        print(total_time)

    # this plots things in log scale (pls google it), you need to add matplotlib to your virtualenv first!

    plt.plot(set_szs, timing,label='wpqu_union')

    ########################5



    plt.xscale('log')
    plt.yscale('log')
    plt.title('log')
    plt.ylabel('some numbers')
    plt.legend()
    plt.show()