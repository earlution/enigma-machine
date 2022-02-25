import unittest
from keyboard import Keyboard


class TestKeyboard(unittest.TestCase):
    def test_press_sml_a(self):
        kb = Keyboard()
        result = kb.press('a')
        self.assertEqual('A', result)

    def test_press_big_a(self):
        kb = Keyboard()
        result = kb.press('A')
        self.assertEqual('A', result)

    def test_press_big_a(self):
        kb = Keyboard()
        result = kb.press('1')
        self.assertEqual('A', result)


if __name__ == '__main__':
    unittest.main()
