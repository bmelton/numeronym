import unittest
from numeronym import Numeronym

class TestNumeronym(unittest.TestCase):
    def setUp(self):
        self.strings = [
            'Andreesen Horowitz',
            'Internationalization',
            'Personalization',
        ]

        self.shorts = [
            'Hi',
            'Hip',
        ]

        self.defaults   = ['a16z', 'i18n', 'p13n', ]
        self.uppers     = ['A16z', 'I18n', 'P13n', ]
        self.short_defs = ['h1', 'h2', ]
        self.short_upper= ['H1', 'H2', ]

    def test_default(self):
        n = Numeronym()
        i = 0
        while i < len(self.strings):
            self.assertEqual(n.encode(self.strings[i]), self.defaults[i])
            i = i+1

        i = 0
        while i < len(self.shorts):
            self.assertRaises(Exception, n.encode, self.shorts[i])
            i = i+1

    def test_short(self):
        n = Numeronym(short=True)
        i = 0
        while i < len(self.strings):
            self.assertEqual(n.encode(self.strings[i]), self.defaults[i])
            i = i+1

        i = 0
        while i < len(self.shorts):
            self.assertEqual(n.encode(self.shorts[i]), self.short_defs[i])
            i = i+1

    def test_upper(self):
        n = Numeronym(preserve_case=True)
        i = 0
        while i < len(self.strings):
            self.assertEqual(n.encode(self.strings[i]), self.uppers[i])
            i = i+1

if __name__ == '__main__':
    unittest.main()
