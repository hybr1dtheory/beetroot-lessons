class Person:
    def __init__(self, f_name: str, l_name: str, age: int):
        self.first_name = f_name
        self.last_name = l_name
        self.age = age
    
    def talk(self):
        print(f"Hello! My name is {self.first_name} {self.last_name}. I`m {self.age} years old.")


class Dog:
    age_factor = 7

    def __init__(self, age: int):
        self.age = age
    
    def human_age(self):
        return self.age * self.age_factor


class TVController:
    def __init__(self, channels: list):
        self.ch_list = channels
        self.__index = 0
    
    def first_channel(self):
        self.__index = 0
        return self.ch_list[0]
    
    def last_channel(self):
        self.__index = len(self.ch_list) - 1
        return self.ch_list[-1]
    
    def turn_channel(self, num: int):
        if 0 < num <= len(self.ch_list):
            self.__index = num - 1
            return self.ch_list[num-1]
        else:
            return "Wrong channel number!"
    
    def next_channel(self):
        self.__index += 1
        if 0 <= self.__index < len(self.ch_list):
            return self.ch_list[self.__index]
        else:
            self.__index -= len(self.ch_list)
            return self.ch_list[self.__index]

    def previous_channel(self):
        self.__index -= 1
        if 0 <= self.__index < len(self.ch_list):
            return self.ch_list[self.__index]
        else:
            self.__index += len(self.ch_list)
            return self.ch_list[self.__index]

    def current_channel(self):
        return self.ch_list[self.__index]

    def exists(self, ch):
        if isinstance(ch, int):
            if 0 < ch <= len(self.ch_list):
                return 'Yes'
            else:
                return 'No'
        elif isinstance(ch, str):
            if ch in self.ch_list:
                return 'Yes'
            else:
                return 'No'
        else:
            return 'Wrong type of channel name!'
