from time import time, localtime


class OpenFile:
    """my context manager for working with files with logging"""
    __opened_files = 0

    def __init__(self, fpath: str, mode='r', encoding='UTF-8'):
        self._path = fpath
        self._mode = mode
        self._encoding = encoding
        self._obj = None

    def __enter__(self):
        self._obj = open(self._path, self._mode, encoding=self._encoding)
        OpenFile.opening(self._path, self._mode)
        return self._obj

    def __exit__(self, ex_type, ex_val, traceback):
        self._obj.close()
        OpenFile.closing(self._path, ex_type, ex_val, traceback)
        return False

    @classmethod
    def opening(cls, name, mode):
        cls.__opened_files += 1
        with open('opening_logs.txt', 'a') as lg:
            lt = localtime(time())
            t = f"{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday}  {lt.tm_hour}:{lt.tm_min} ---> "
            lg.write(f"{t} open file '{name}' with mode '{mode}'\n")

    @classmethod
    def closing(cls, name, *args):
        cls.__opened_files -= 1
        with open('opening_logs.txt', 'a') as lg:
            lt = localtime(time())
            t = f"{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday}  {lt.tm_hour}:{lt.tm_min} ---> "
            details = f"Type: {args[0]}, Value: {args[1]}, {args[2]}"
            lg.write(f"{t} close file '{name}'. Exception details: {details} \n")

    @classmethod
    def get_count(cls):
        return cls.__opened_files


if __name__ == "__main__":
    print(OpenFile.get_count())
    with OpenFile('my_file.txt') as fr:
        text = fr.read()
        print(text)
        print(OpenFile.get_count())
    print(OpenFile.get_count())
