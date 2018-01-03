import random


def generate_random_example( dir, name):


    #we define a random size for a bin
    output = "Taille bin\n"
    output += str(random.randint(10, 1000)) + "\n"

    #we create objects
    output += "Objets\n"
    nb_object = random.randint(1, 10000)
    for i in range(0, nb_object-1):
        output += str(random.randint(1, 1000)) + ", "
    output += str(random.randint(1, 1000)) + "."

    example_file = open(dir + '/' + name + str(nb_object) +".txt", 'w')
    example_file.write(output)
    example_file.close()

generate_random_example("../example", "example")
