import string

class Plugboard:
    def __init__(self):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        self.mappings = {k: v for k, v in zip(uppercase_letters_list, uppercase_letters_list)}
        self.plugleads = list()
        self.__max_num_of_plugleads = 10
        self.__num_of_plugleads = 0

    def add(self, pluglead):
        if len(self.plugleads) == self.__max_num_of_plugleads:
            pass
            # @TODO imp. better error handling here
            # print('No available plugleads')
            # raise PermissionError  # don't have permission to add another lead
        else:
            self.plugleads.append(pluglead)
            self.mappings.update(pluglead.mappings)
            self.__num_of_plugleads += 1

    # @TODO imp. un_patch: delete from self.plugleads; reset self.mappings
    def un_patch(self, letter):
        raise NotImplementedError

    def encode(self, letter):
        """Encodes param letter

        Ecoding of the letter depends on the current state of the plugboard. I.e. what - if any - patches have beem
        made.

        :param letter: the letter to be encoded
        :return: the encoded letter
        """
        return self.mappings[letter]

class PlugLead:
    def __init__(self, patch):
        patch = patch.upper()
        self.mappings = dict()
        self.mappings = {patch[0]: patch[1], patch[1]: patch[0]}
        # @TODO evel. if there is a overlap of functionality here...
        self.mapping1 = dict()
        self.mapping1 = {patch[0]: patch[1]}
        self.mapping2 = dict()
        self.mapping2 = {patch[1]: patch[0]}

    def encode(self, letter):
        if letter.upper() in self.mappings:
            return self.mappings[letter]
        else:
            return letter.upper()


if __name__ == "__main__":
    pass
