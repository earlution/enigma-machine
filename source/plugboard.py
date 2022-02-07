import string
from pluglead import PlugLead


class Plugboard:
    def __init__(self):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        self.mappings = [{k: v} for k, v in zip(uppercase_letters_list, uppercase_letters_list)]
        self.__max_num_of_plugleads = 10
        self.__num_of_plugleads = 0
        self.__plugleads = [{key} for key in range(1, 11)]

    def patch(self, pluglead: PlugLead):
        if self.__num_of_plugleads <= 10:
            self.mappings.update(pluglead)
        else:
            # @TODO imp. better error handling here
            print('No available plugleads')
            raise PermissionError  # don't have permission to add another lead?
