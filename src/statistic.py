import os
import glob
from collections import namedtuple, defaultdict

Output = namedtuple('Output', ('name', 'input', 'time', 'score', 'bins'))


def parse(file):
    name, filename, time, score, *bins = file.read().splitlines()
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
    with open('../output/statistics-time.csv', 'w') as time, open('../output/statistics-nb-bin.csv', 'w') as score:
        time.write(';' + ';'.join(algorithm for algorithm in algorithms) + '\n')
        score.write(';' + ';'.join(algorithm for algorithm in algorithms) + '\n')
        for in_file in input_file:
            time.write(f'{in_file}')
            score.write(f'{in_file}')
            for algorithm in algorithms:
                time.write(f';{outputs[algorithm][in_file].time}'.replace('.', ','))
                score.write(f';{outputs[algorithm][in_file].score}')
            time.write('\n')
            score.write('\n')
        time.write('average')
        score.write('average')
        for algorithm in algorithms:
            times = list(output.time for output in outputs[algorithm].values())
            bins = list(output.score for output in outputs[algorithm].values())
            time.write(f';{sum(times) / len(times)}'.replace('.', ','))
            score.write(f';{sum(bins) / len(bins)}'.replace('.', ','))
        time.write('\n')
        score.write('\n')




if __name__ == '__main__':
    main()
