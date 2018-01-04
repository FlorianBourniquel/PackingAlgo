from source.items import object

class example:

    def __init__(self, example_filepath):
        example = open(example_filepath, "r")
        example.readline()
        self._bin_size = int(example.readline())
        example.readline()
        objects_size = example.readline().replace(".", "").split(", ")
        self._items = []
        for object_size in objects_size:
            self._items.append(object(int(object_size)))

    def _get_bin_size(self):
        return self._bin_size

    def _get_objects(self):
        return self._items

    items = property(_get_objects)
    bin_size = property(_get_bin_size)