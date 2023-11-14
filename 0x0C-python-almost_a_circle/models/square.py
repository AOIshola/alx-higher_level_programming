#!/usr/bin/python3
"""The Square Module"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a Square Object"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        self.x = x
        self.y = y
        self.id = id
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Implements str() for the object
        [Rectangle] (<id>) <x>/<y> - <size>
        """
        return ("[" + type(self).__name__ + "] " + "(" + str(self.id) + ") " +
                str(self.x) + "/" + str(self.y) + " - " +
                str(self.__size))

    @property
    def size(self):
        """Getter for Size attribute"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """Update a Square Object"""
        if len(args) > 3:
            self.y = args[3]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 1:
            self.__size = args[1]
        if len(args) >= 1:
            self.id = args[0]
        if len(args) == 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.__size = value
                elif key == "x":
                    self.x = value
                else:
                    self.y = value

    def to_dictionary(self):
        """Converts Class to dictionary"""
        my_keys = ({attr: getattr(self, str(attr)) for attr in dir(self) if
                    not callable(getattr(self, attr)) and
                    not attr.startswith("__") and not attr.startswith("_") and
                    attr != "height" and attr != "width"})
        return (my_keys)
