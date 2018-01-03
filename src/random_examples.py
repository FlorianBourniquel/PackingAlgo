import random


def generate_random_example( dir, name):
    example_file = open(dir + name, 'w')
    example_file.write("Taille bin\n")
    example_file.write(str(random.randint(1, 1000)) + "\n")
    example_file.write("Objets\n")

    nb_object = random.randint(1, 10000)
    random_size_objects = []
    for i in range(0, nb_object):
        example_file.write(str(random.randint(1, 1000)) + ", ")


    example_file.close()

generate_random_example("../example", "example")
