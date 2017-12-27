from src.fit_strategy import fit_strategy
from src.bin import bin

class next_fit(fit_strategy):

    def __init__(self, example):
        fit_strategy.__init__(self, example)

    def execute_strategy(self):
        self.bins.append(bin(self.example.bin_size))
        for item in self.example.items:
            if self.bins[len(self.bins) - 1].have_enough_space_available(item.size):
                self.bins[len(self.bins) - 1].addObject(item)
            else:
                self.bins.append(bin(self.example.bin_size))
                self.bins[len(self.bins) - 1].addObject(item)

