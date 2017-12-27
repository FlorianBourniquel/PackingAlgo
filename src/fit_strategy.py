from abc import abstractmethod

class fit_strategy:

    def __init__(self, example):
        self.example = example
        self.bins = []

    @abstractmethod
    def execute_strategy(self):
        pass

    def __str__(self) -> str:
        content = ""
        for i, bin in enumerate(self.bins, 1):
            content += "bin N°" + str(i) + "\n"
            content += bin.__str__() + "\n"
        return content

