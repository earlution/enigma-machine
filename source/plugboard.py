import string

class Plugboard:
    def __init__(self):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        self.mappings = {k: v for k, v in zip(uppercase_letters_list, uppercase_letters_list)}
        # to do imp. self.plugleads
        self.plugleads = list()
        self.__max_num_of_plugleads = 10
        self.__num_of_plugleads = 0

    def patch(self, source, target):
        if len(self.plugleads) <= self.__max_num_of_plugleads:
            self.__num_of_plugleads += 1
            pluglead = Pluglead(source.upper(), target.upper())
            self.plugleadsappend(pluglead)
            self.mappings.update(pluglead.mapping1)
            self.mappings.update(pluglead.mapping2)
        else:
            # @TODO imp. better error handling here
            print('No available plugleads')
            raise PermissionError  # don't have permission to add another lead

    # @TODO imp. un_patch: delete from self.plugleads; reset self.mappings
    def un_patch(self, letter):
        raise NotImplementedError

class Pluglead:
    def __init__(self, source, target):
        self.mapping1 = dict()
        self.mapping1 = {source: target}
        self.mapping2 = dict()
        self.mapping2 = {target: source}
