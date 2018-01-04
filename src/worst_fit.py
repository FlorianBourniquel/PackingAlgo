import sys

from src.fit_strategy import fit_strategy
from src.bin import bin

class worst_fit(fit_strategy):

    def __init__(self, example):
        fit_strategy.__init__(self, example)

    def execute_strategy(self):
        self.bins.append(bin(self.example.bin_size))
        for item in self.example.items:
            min = sys.maxsize
            for a_bin in self.bins:
                if a_bin.level < min:
                    min = a_bin.level
                    bin_minlevel = a_bin
            if bin_minlevel.have_enough_space_available(item.size):
                bin_minlevel.addObject(item)
            else:
                self.bins.append(bin(self.example.bin_size))
                self.bins[len(self.bins) - 1].addObject(item)