from source.first_fit import first_fit
from source.example import example
from source.next_fit import next_fit
from source.worst_fit import worst_fit
import timeit

example_1 = example("exemples/exemple100.txt")
#fit = next_fit(example_1)
fit = worst_fit(example_1)
#fit = first_fit(example_1)

fit.execute_strategy()

print(fit)
