def prepare_alphabet(file_path="morse_alphabet.txt"):
    with open(file_path, "r") as f:
        raw_data = f.read().split('\n')
    result_dictionary = {word[0]: word.split(" ")[1] for word in raw_data}
    return result_dictionary


__MORSE_ALPHABET = prepare_alphabet()


def allowed_to_encode(text):
    for letter in text.upper():
        if not (letter in __MORSE_ALPHABET.keys()) and ord(letter) != 13 and ord(letter) != 10 and letter != ' ':
            return False
    return True


def encode_message(text):
    encoded_text = ""
    for letter in text.upper():
        encoded_letter = __MORSE_ALPHABET.get(letter)
        if encoded_letter is None:
            if ord(letter) != 13 and ord(letter) != 10:
                encoded_text += "/ "
        else:
            encoded_text += f"{encoded_letter} "
    return encoded_text[:-1]
