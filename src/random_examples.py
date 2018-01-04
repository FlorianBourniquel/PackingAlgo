import random
import os


class random_example:

    def __init__(self, bin_size, min_object_size, max_object_size, nb_objects):
        self._bin_size = bin_size
        self._min_object_size = min_object_size
        self._max_object_size = max_object_size
        self._nb_objects = nb_objects
        self._objects = []
        self._check_attributes()
        self._generate()

    def _check_attributes(self):
        self._check_bin_size()
        self._check_min_object_size()
        self._check_max_object_size()
        self._check_nb_objects()

    def _check_bin_size(self):
        assert self._bin_size > 0

    def _check_min_object_size(self):
        assert 0 < self._min_object_size <= self._bin_size

    def _check_max_object_size(self):
        assert 0 < self._max_object_size <= self._bin_size and self._max_object_size >= self._min_object_size

    def _check_nb_objects(self):
        assert self._nb_objects > 0

    def __str__(self):
        output = "Taille bin\n"
        output += str(self._bin_size) + "\n"
        output += "Objets\n"
        for i in range(self._nb_objects - 1):
            output += str(self._objects[i]) + ", "
        output += str(self._objects[-1]) + ".\n"
        return output


    def _generate(self):
        for i in range(self._nb_objects):
            self._objects.append(random.randint(self._min_object_size, self._max_object_size))


def generate_random_example():
    print("Entrer le nombre d exemple a generer")
    nb_examples = int(input())

    print("Entrer la taille des bins")
    bin_size = int(input())

    print("Entrer la taille minimale des objets")
    min_object_size = int(input())

    print("Entrer la taille maximale des objets")
    max_object_size = int(input())

    print("Entrer le nombre d objets")
    nb_objects = int(input())

    if not os.path.exists('../random_example'):
        os.mkdir('../random_example')

    for i in range(nb_examples):
        example = random_example(bin_size, min_object_size, max_object_size, nb_objects)
        example_file = open("../random_example/example" + str(i) + "-" + str(nb_objects), 'w')
        example_file.write(str(example))
        example_file.close()

generate_random_example()
