def prepare_alphabet(file_path="morse_alphabet.txt"):
    with open(file_path, "r") as f:
        raw_data = f.read().split('\n')
    result_dictionary = {word[0]: word.split(" ")[1] for word in raw_data}
    return result_dictionary


__ENCODE_MORSE_ALPHABET = prepare_alphabet()
__DECODE_MORSE_ALPHABET = {v: k for k, v in __ENCODE_MORSE_ALPHABET.items()}


def allowed_to_encode(text):
    for letter in text.upper():
        if not (letter in __ENCODE_MORSE_ALPHABET.keys()) and ord(letter) != 13 and ord(letter) != 10 and letter != ' ':
            return False
    return True


def encode_message(text):
    encoded_text = ""
    for letter in text.upper():
        encoded_letter = __ENCODE_MORSE_ALPHABET.get(letter)
        if encoded_letter is None:
            if ord(letter) != 13:
                encoded_text += "/ "
        else:
            encoded_text += f"{encoded_letter} "
    return encoded_text[:-1]


def allowed_to_decode(words):
    for word in words:
        for letter in word.split(" "):
            if not (letter in __DECODE_MORSE_ALPHABET):
                return False
    return True


def decode_message(words):
    decoded_message = ""
    for word in words:
        for letter in word.split(" "):
            decoded_message += __DECODE_MORSE_ALPHABET[letter]
        decoded_message += " "
    return  decoded_message
