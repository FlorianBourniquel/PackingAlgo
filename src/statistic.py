import os
import glob
from collections import namedtuple, defaultdict

Output = namedtuple('Output', ('name', 'input', 'time', 'score', 'bins'))


def parse(file):
    name, filename, time, score, *bins = file.read().splitlines()
    print(name, filename, time, score, bins)
    return Output(name, filename, float(time), int(score),
                  [list(map(int, line.split(', '))) for line in bins])


def main():
    input_file = set()

    outputs = defaultdict(dict)
    for filename in glob.glob('../output/*.txt'):
        with open(filename) as file:
            output = parse(file)
            input_file.add(output.input)
            outputs[output.name][output.input] = output
    algorithms = list(outputs)
    with open('../output/statistics.csv', 'w') as stats:
        stats.write(';' + ';;'.join(algorithm for algorithm in algorithms) + '\n')
        stats.write(';time;nb bin' * len(algorithms) + '\n')
        for in_file in input_file:
            stats.write(f'{in_file}')
            for algorithm in algorithms:
                stats.write(f';{outputs[algorithm][in_file].time};{outputs[algorithm][in_file].score}'.replace('.', ','))
            stats.write('\n')
        stats.write('average')
        for algorithm in algorithms:
            times = list(output.time for output in outputs[algorithm].values())
            bins = list(output.score for output in outputs[algorithm].values())
            stats.write(f';{sum(times) / len(times)};{sum(bins) / len(bins)}'.replace('.', ','))


if __name__ == '__main__':
    main()
