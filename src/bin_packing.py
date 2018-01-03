import bisect
import glob
import os
import time
from abc import abstractmethod
from typing import List


def parse(file):
    text1, size, text2, items = file.readlines()
    return int(size), list(map(int, items.replace('.\n', '').split(',')))


def output(filename, fit, duration):
    """
        Output format:
            the name of the algorithm
            the name of the input file
            the required time to compute the solution
            n the number of bin used
            On the following n lines, the items in each bin separated by a ", "
            the file ends with a \n
    """
    if not os.path.exists('../output'):
        os.mkdir('../output')
    with open(f'../output/{fit.__class__.__name__}-{os.path.basename(filename)}', 'w') as out:
        out.write(f'{fit.__class__.__name__}\n{os.path.basename(filename)}\n{duration}\n{fit}\n')


class BinOverflow(Exception):
    pass


class Bin:
    def __init__(self, size):
        self.size = size
        self.level = 0
        self.items = []

    def add_item(self, item):
        if self.have_enough_space_available(item):
            self.level += item
            self.items.append(item)
        else:
            raise BinOverflow()

    def have_enough_space_available(self, item):
        return self.size >= self.level + item

    def __lt__(self, other):
        return self.level < other.level

    def __gt__(self, other):
        return self.level > other.level

    def __str__(self):
        return ', '.join(map(str, self.items))

    def __repr__(self):
        return f'Bin({self.level}, {self.items})'


class Fit:
    """
        A superclass for the fit algorithms
        All the subclasses of this class are stored in the algorithms field
    """
    algorithms = []

    def __init_subclass__(cls, **kwargs):
        Fit.algorithms.append(cls)

    def __init__(self, size, items):
        self.size = size
        self.items = items
        self.bin: List[Bin] = []

    def add_bin(self):
        self.bin.append(Bin(self.size))

    @abstractmethod
    def apply(self):
        pass

    def __str__(self):
        return f"{len(self.bin)}\n" + '\n'.join(map(str, self.bin))


class FirstFit(Fit):
    def apply(self):
        self.add_bin()
        for item in self.items:
            for currentBin in self.bin:
                if currentBin.have_enough_space_available(item):
                    currentBin.add_item(item)
                    break
            else:
                self.add_bin()
                self.bin[-1].add_item(item)
        return self


class NextFit(Fit):
    def apply(self):
        self.add_bin()
        for item in self.items:
            if self.bin[-1].have_enough_space_available(item):
                self.bin[-1].add_item(item)
            else:
                self.add_bin()
                self.bin[-1].add_item(item)
        return self


class BestFit(Fit):
    """
        The bins in self.bin are sorted in ascending order
    """

    def apply(self):
        self.add_bin()
        for item in self.items:
            position = self.find_best_fit(item)
            if position == -1:
                target_bin = Bin(self.size)
            elif position < len(self.bin):
                target_bin = self.bin.pop(position)
            target_bin.add_item(item)
            bisect.insort_right(self.bin, target_bin)
        return self

    def find_best_fit(self, item):
        lo, hi = 0, len(self.bin)
        while lo < hi:
            mid = (lo + hi) // 2
            if not self.bin[mid].have_enough_space_available(item):
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


class AlmostWorstFit(Fit):
    """
        The bins in self.bin are sorted in ascending order
    """

    def apply(self):
        self.add_bin()
        for item in self.items:
            if len(self.bin) >= 2 and self.bin[1].have_enough_space_available(item):
                target_bin = self.bin.pop(1)
            elif self.bin[0].have_enough_space_available(item):
                target_bin = self.bin.pop(0)
            else:
                target_bin = Bin(self.size)
            target_bin.add_item(item)
            bisect.insort_right(self.bin, target_bin)
        return self


class WorstFit(Fit):
    """
        The bins in self.bin are sorted in ascending order
    """

    def apply(self):
        self.add_bin()
        for item in self.items:
            if self.bin[0].have_enough_space_available(item):
                target_bin = self.bin.pop(0)
            else:
                target_bin = Bin(self.size)
            target_bin.add_item(item)
            bisect.insort_right(self.bin, target_bin)
        return self


def main():
    for filename in glob.glob('../example/*.txt'):
        with open(filename) as source:
            size, items = parse(source)
            for algorithm in Fit.algorithms:
                start = time.clock()
                solution = algorithm(size, items).apply()
                output(filename, solution, (time.clock() - start) * 1000)


if __name__ == '__main__':
    main()
