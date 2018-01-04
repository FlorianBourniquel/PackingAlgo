from source.fit_strategy import fit_strategy
from source.bin import bin

class first_fit(fit_strategy):

    def __init__(self, example):
        fit_strategy.__init__(self, example)

    def execute_strategy(self):
        self.bins.append(bin(self.example.bin_size))
        for item in self.example.items:
            for currentBin in self.bins:
                if currentBin.have_enough_space_available(item.size):
                    currentBin.addObject(item)
                    break
            else:
                self.bins.append(bin(self.example.bin_size))
                self.bins[len(self.bins) - 1].addObject(item)

