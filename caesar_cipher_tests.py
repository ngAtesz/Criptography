import unittest
from caesar_cipher import AteszCaesarCipher


class AteszCaesarCipherTests(unittest.TestCase):
    def test_init_shiftIsOne_shiftPropertySetToOne(self):
        cipher = AteszCaesarCipher(1)
        self.assertEqual(1, cipher.shift)

    def test_encode_shiftIsZero_returnsWithTheGivenText(self):
        cipher = AteszCaesarCipher(0)
        encoded_text = cipher.encode("a")
        self.assertEqual("a", encoded_text)

    def test_encode_shiftIsOne_returnsWithCharacterShiftedWithOne(self):
        # Arrange
        cipher = AteszCaesarCipher(1)
        # Act
        encoded_text = cipher.encode("a")
        # Assert
        self.assertEqual("b", encoded_text)


if __name__ == '__main__':
    unittest.main()
