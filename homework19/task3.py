class MutStr:
    """Implements a mutable string based on list"""
    def __init__(self, string=""):
        if isinstance(string, str):
            self.__string = list(string)
        else:
            raise ValueError("Argument must be a string")

    def __len__(self):
        return len(self.__string)

    def __str__(self):
        return "".join(self.__string)

    def __getitem__(self, key: int):
        return self.__string[key]

    def __setitem__(self, key: int, value: str):
        if not isinstance(value, str) or len(value) != 1:
            raise ValueError("Value must be a one-character string")
        self.__string[key] = value

    def __delitem__(self, key):
        del self.__string[key]

    def __iter__(self):
        return iter(self.__string)

    def append(self, value: str):
        if not isinstance(value, str) or len(value) != 1:
            raise ValueError("Value must be a one-character string")
        self.__string.append(value)


if __name__ == "__main__":
    my_str = MutStr("Hello, world")
    print(my_str)
    # we can change str now
    my_str[7] = 'W'
    my_str.append('!')
    print(my_str)
    # iterate through my own collection
    for c in my_str:
        print(c)
