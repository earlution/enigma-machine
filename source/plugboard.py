import string


class PlugLead:
    def __init__(self, patch):
        patch = patch.upper()
        self.mappings = dict()
        self.mappings = {patch[0]: patch[1], patch[1]: patch[0]}

    def encode(self, letter):
        if letter.upper() in self.mappings:
            return self.mappings[letter]
        else:
            return letter.upper()


class Plugboard:
    def __init__(self):
        uppercase_letters_string = string.ascii_uppercase
        uppercase_letters_list = list(uppercase_letters_string)
        self.mappings = {k: v for k, v in zip(uppercase_letters_list, uppercase_letters_list)}
        self.patchings = dict()
        self.plugleads = list()
        self.__max_num_of_plugleads = 10
        self.__num_of_plugleads = 0

    def add(self, pluglead: PlugLead):
        """Add one of ten available PlugLeads to the Plugboard.

        Patches two letters specified in the name parameter of the PlugLead.  E.g. the PlugLead argument 'AB' would
        patch the letters 'A' abd 'B', so that 'A' would be encoded to 'B' and 'B' would be encoded to 'A'.

        :param pluglead: A PlugLead object specifying the two letters for a bidirectional patch.
        :type pluglead: PlugLead
        """

        # edge case: attempt to make a patch that utilises an already patched letter
        for i in pluglead.mappings:
            for j in self.patchings:
                if i == j:
                    raise ValueError
        # edge case: attempt to add more than 10 PlugLeads
        if len(self.plugleads) == self.__max_num_of_plugleads:
            raise ValueError
        else:
            self.plugleads.append(pluglead)
            self.mappings.update(pluglead.mappings)
            self.patchings.update(pluglead.mappings)
            self.__num_of_plugleads += 1

    # @TODO imp. un_patch: delete from self.plugleads; reset self.mappings
    def un_patch(self, pluglead: PlugLead):
        if not isinstance(pluglead, PlugLead):
            pass
        elif pluglead not in self.plugleads:
            pass
        else:
            self.plugleads.remove(pluglead)

    def encode(self, letter):
        """Encodes param letter

        Encoding of the letter depends on the current state of the plugboard. I.e. what - if any - patches have beem
        made.

        :param letter: the letter to be encoded
        :return: the encoded letter
        """
        return self.mappings[letter]


if __name__ == "__main__":
    pass
