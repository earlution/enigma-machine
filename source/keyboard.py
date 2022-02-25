class Keyboard:
    def __init__(self):
        pass

    def press(self, letter=None):
        if type(letter) != str or (ord(letter.upper()) < 65 or (ord(letter.upper()) > 90)):
            letter = input('Type a letter: ').upper()[0]
            if type(letter) != str or (ord(letter.upper()) < 65 or (ord(letter.upper()) > 90)):
                return ''
        else:
            return letter.upper()

