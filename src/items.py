class object:

    def __init__(self, size):
        self._size = size

    def _get_size(self):
        return self._size

    size = property(_get_size)