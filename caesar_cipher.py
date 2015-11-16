from string import ascii_lowercase, ascii_uppercase


class AteszCaesarCipher:
    max_length = len(ascii_lowercase)

    def __init__(self, shift):
        self.shift = shift

    def encode(self, sentence: str):
        result = ""

        for char in sentence:
            lower_char = char.lower()
            if lower_char in ascii_lowercase:
                index = self._get_ciphered_index_for(lower_char)
                result += self._get_ciphered_char(char, index)
            else:
                result += char

        return result

    def _get_ciphered_index_for(self, lower_char):
        index = ascii_lowercase.find(lower_char) + self.shift
        if index >= self.max_length:
            index -= self.max_length

        if index < 0:
            index += self.max_length

        return index

    def _get_ciphered_char(self, char, index):
        if char.islower():
            return ascii_lowercase[index]
        else:
            return ascii_uppercase[index]


if __name__ == '__main__':
    decoded_sentence = "Guido van Rossum!"
    cipher_encoder = AteszCaesarCipher(13)
    encoded = cipher_encoder.encode(decoded_sentence)
    print(encoded)
    cipher_decoder = AteszCaesarCipher(-13)
    print(cipher_decoder.encode(encoded))
