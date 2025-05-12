def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('lm') returns 'hi'
    decrypt('ewhjklnop') returns 'asdfghjkl'
    decrypt('kj') returns 'gf'
    decrypt('ix') returns 'et'
    """

def main():
    """Create a function main that takes no arguments and returns no
    values. This function should call the encrypt and decrypt functions
    and print the results.
    """

if __name__ == '__main__':
    main()
/hw04/hw04_test.py
import unittest
from hw04 import *

class TestHW04(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_decrypt(self):
        self.assertEqual(decrypt('lm'), 'hi')
        self.assertEqual(decrypt('ewhjklnop'), 'asdfghjkl')
        self.assertEqual(decrypt('kj'), 'gf')
        self.assertEqual(decrypt('ix'), 'et')

if __name__ == '__main__':
    unittest.main()
/hw03/hw03_test.py
import unittest
from hw03 import *

class TestHW03(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt('hi'), 'lm')
        self.assertEqual(encrypt('asdfghjkl'), 'ewhjklnop')
        self.assertEqual(encrypt('gf'), 'kj')
        self.assertEqual(encrypt('et'), 'ix')

    def test_decrypt(self):
        self.assertEqual(decrypt('lm'), 'hi')
        self.assertEqual(decrypt('ewhjklnop'), 'asdfghjkl')
        self.assertEqual(decrypt('kj'), 'gf')
        self.assertEqual(decrypt('ix'), 'et')

if __name__ == '__main__':
    unittest.main()
/hw02/hw02.py
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """

def decrypt(s):
    """Create a function decrypt that takes a string as an argument and
    returns a string decrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    decrypt('lm') returns 'hi'
    decrypt('ewhjklnop') returns 'asdfghjkl'
    decrypt('kj') returns 'gf'
    decrypt('ix') returns 'et'
    """

def main():
    """Create a function main that takes no arguments and returns no
    values. This function should call the encrypt and decrypt functions
    and print the results.
    """

if __name__ == '__main__':
    main()
/hw01/hw01.py
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with