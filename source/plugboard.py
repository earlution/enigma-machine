import string

class Plugboard:
    def __init__(self):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        self.mappings = {k: v for k, v in zip(uppercase_letters_list, uppercase_letters_list)}
        self.plugleads = list()
        self.__max_num_of_plugleads = 10
        self.__num_of_plugleads = 0

    def patch(self, source, target):
        if len(self.plugleads) == self.__max_num_of_plugleads:
            # @TODO imp. better error handling here
            print('No available plugleads')
            # raise PermissionError  # don't have permission to add another lead
        else:
            pluglead = Pluglead(source.upper(), target.upper())
            self.plugleads.append(pluglead)
            self.mappings.update(pluglead.mapping1)
            self.mappings.update(pluglead.mapping2)
            self.__num_of_plugleads += 1



    # @TODO imp. un_patch: delete from self.plugleads; reset self.mappings
    def un_patch(self, letter):
        raise NotImplementedError

class Pluglead:
    def __init__(self, source, target):
        self.mapping1 = dict()
        self.mapping1 = {source: target}
        self.mapping2 = dict()
        self.mapping2 = {target: source}


if __name__ == "__main__":
    from plugboard import *
    pb = Plugboard()
    pb.patch('a', 'b')
    pb.patch('C', 'K')
    pb.patch('E', 'F')
    pb.patch('G', 'H')
    pb.patch('I', 'J')
    pb.patch('D', 'L')
    pb.patch('M', 'N')
    pb.patch('O', 'P')
    pb.patch('Q', 'R')
    pb.patch('S', 'U')
    pb.patch('X', 'Z')
