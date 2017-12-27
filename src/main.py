from first_fit import first_fit
from src.example import example
from src.next_fit import next_fit
from src.worst_fit import worst_fit
import timeit

example_1 = example("../example/exemple500.txt")
#fit = next_fit(example_1)
#fit = worst_fit(example_1)
fit = first_fit(example_1)

fit.execute_strategy()

print(fit)
