class Keyboard:
    def __init__(self):
        pass

    def press(self, letter=None):
        if type(letter) != str:
            return input('Type a letter: ').upper()[0]
        else:
            return letter

