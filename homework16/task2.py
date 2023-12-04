class Mathematician:
    """Math operations with iterable objects of numbers"""
    @staticmethod
    def square_nums(nums):
        return [i**2 for i in nums]

    @staticmethod
    def remove_positives(nums):
        return [i for i in nums if i <= 0]

    @staticmethod
    def is_leapyear(year: int):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def filter_leaps(self, years):
        """takes an iterable of years (integers) and removes those that are not 'leap years'"""
        return [y for y in years if self.is_leapyear(y)]
