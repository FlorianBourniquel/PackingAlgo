class bin:

    def __init__(self, size):
        self._level = 0
        self._size = size
        self.items = []

    def addObject(self, item):
        self.items.append(item)
        self._level += item.size

    def _get_level(self) -> int:
        return self._level

    def have_enough_space_available(self, object_size) -> bool:
        return self._size >= (object_size + self._level)

    def __str__(self) -> str:
        content = ""
        for i, item in enumerate(self.items, 1):
            content = content + str(i) + ": " + str(item.size) + "\n"
        return content

    level = property(_get_level)
