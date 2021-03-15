import unittest
from exo1 import * 
from exo2 import * 
from exo3 import * 
from exo4 import * 
from exo5 import * 
from exo6 import * 
from exo7 import * 

class TestStringMethods(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse('simplon'), 'nolpmis')
        self.assertEqual(reverse('slt'), 'tls')

    def test_reverse_number(self):
        self.assertEqual(reverse_number(20), -20)
        self.assertEqual(reverse_number(-200), 200)

    def test_reverse_num(self):
        self.assertEqual(reverse_num(422), 224)
        self.assertEqual(reverse_num(357), 753)
    def test_count_word(self):
        self.assertEqual(count_word("Ici, c'est Simplon !!"), 3)
    def test_count_moy_word(self):
        self.assertEqual(count_moy_word("salut youcef"), 5.5)
        self.assertEqual(count_moy_word("Ici, c'est Simplon !!"), 4.7)
    def test_palindrom(self):
        self.assertEqual(palindrom("aba"), "oui")
        self.assertEqual(palindrom("youcef"), "non")
    def test_duplicate(self):
        self.assertEqual(duplicate([2,3,"abc",3,4,"ab",2]), [2, 3])

if __name__ == '__main__':
    unittest.main()