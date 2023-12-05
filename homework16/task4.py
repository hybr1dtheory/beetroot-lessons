from time import time, localtime


class NotInRangeError(Exception):
    """logs every error message to a file named 'logs.txt'."""
    def __init__(self, msg='', value=''):
        self.message = msg
        self.value = value
        with open("logs.txt", "a") as logs:
            lt = localtime(time())
            t = f"{lt.tm_year}-{lt.tm_mon}-{lt.tm_mday}  {lt.tm_hour}:{lt.tm_min} ---> "
            logs.write(f"{t}NotInRangeError for value {self.value} was raised with message: {self.message}\n")

    def __str__(self):
        return f"Value {self.value} is not in range! \n{self.message}"


def test_except(val, low, high):
    if low <= val <= high:
        return val
    else:
        raise NotInRangeError(f"Value must be in range: {low} <= value <= {high}", val)
