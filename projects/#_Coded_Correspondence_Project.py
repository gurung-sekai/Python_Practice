# Task 1: Decode Vishal's first Caesar Cipher message

alphabet = "abcdefghijklmnopqrstuvwxyz"

message = """xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. 
muhu oek qrbu je tusetu yj? y xefu ie! 
iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"""

offset = 10

decoded_message = ""

# Look at each character in the encrypted message
for character in message:

    # Only change characters that are letters
    if character in alphabet:

        # Find the current position of the letter
        old_index = alphabet.find(character)

        # Move 10 positions to the RIGHT to decode
        new_index = (old_index + offset) % 26

        # Add the decoded letter to our result
        decoded_message += alphabet[new_index]

    else:
        # Keep spaces, punctuation, etc. unchanged
        decoded_message += character

print(decoded_message)

# Task 2: Encode a message using an offset of 10

alphabet = "abcdefghijklmnopqrstuvwxyz"

message_to_vishal = "hello vishal! this cipher is really cool!"
offset = 10

encoded_message = ""

for character in message_to_vishal:

    # Only encode letters
    if character in alphabet:

        # Find the current position
        old_index = alphabet.find(character)

        # Move 10 places to the LEFT to encode
        new_index = (old_index - offset) % 26

        # Add the encoded character
        encoded_message += alphabet[new_index]

    else:
        # Leave punctuation and spaces unchanged
        encoded_message += character

print(encoded_message)

# Task 3: Reusable Caesar Cipher functions

alphabet = "abcdefghijklmnopqrstuvwxyz"


def caesar_decode(message, offset):
    decoded_message = ""

    for character in message:

        # Only shift letters
        if character in alphabet:
            old_index = alphabet.find(character)

            # Decoding shifts to the RIGHT
            new_index = (old_index + offset) % 26

            decoded_message += alphabet[new_index]

        else:
            # Keep spaces and punctuation
            decoded_message += character

    return decoded_message


def caesar_encode(message, offset):
    encoded_message = ""

    for character in message:

        # Only shift letters
        if character in alphabet:
            old_index = alphabet.find(character)

            # Encoding shifts to the LEFT
            new_index = (old_index - offset) % 26

            encoded_message += alphabet[new_index]

        else:
            # Keep spaces and punctuation
            encoded_message += character

    return encoded_message


# First encrypted message
first_message = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."

# We already know this one has an offset of 10
print(caesar_decode(first_message, 10))

second_message = """bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd
yqeemsqe ue qhqz yadq eqogdq!"""

# Decode using the hint from the first message
print(caesar_decode(second_message, 14))

# Task 4: Brute-force a Caesar Cipher

coded_message = """vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl
tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx
by px ptgm mh dxxi hnk fxlltzxl ltyx."""

# There are only 26 possible Caesar Cipher offsets
for offset in range(26):

    print("Offset:", offset)

    # Try decoding using the current offset
    print(caesar_decode(coded_message, offset))

    print(caesar_decode(coded_message, 7))

# Task 5: Vigenere Cipher decoder

alphabet = "abcdefghijklmnopqrstuvwxyz"


def vigenere_decode(message, keyword):

    decoded_message = ""

    # Tracks which keyword letter we are currently using
    keyword_index = 0

    for character in message:

        # Only decode letters
        if character in alphabet:

            # Find the position of the encrypted letter
            message_index = alphabet.find(character)

            # Get the current keyword character
            keyword_character = keyword[
                keyword_index % len(keyword)
            ]

            # Convert keyword character into a shift amount
            keyword_shift = alphabet.find(keyword_character)

            # Decode by shifting to the RIGHT
            new_index = (message_index + keyword_shift) % 26

            decoded_message += alphabet[new_index]

            # Only move to the next keyword letter
            # when we process an actual alphabetic character
            keyword_index += 1

        else:
            # Spaces and punctuation stay unchanged
            decoded_message += character

    return decoded_message


coded_message = """txm srom vkda gl lzlgzr qpdb? fepb ejac!
ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"""

keyword = "friends"

print(vigenere_decode(coded_message, keyword))

# Task 6: Vigenere Cipher encoder

alphabet = "abcdefghijklmnopqrstuvwxyz"


def vigenere_encode(message, keyword):

    encoded_message = ""

    # Keeps track of the current keyword letter
    keyword_index = 0

    for character in message:

        # Only encode letters
        if character in alphabet:

            # Find the message letter's position
            message_index = alphabet.find(character)

            # Select the correct keyword character
            keyword_character = keyword[
                keyword_index % len(keyword)
            ]

            # Find how far we need to shift
            keyword_shift = alphabet.find(keyword_character)

            # Encoding shifts to the LEFT
            new_index = (message_index - keyword_shift) % 26

            encoded_message += alphabet[new_index]

            # Move to the next keyword character
            keyword_index += 1

        else:
            # Do not encode spaces or punctuation
            encoded_message += character

    return encoded_message


# Message we want to send Vishal
my_message = "hello vishal! cryptography is fun."

# Keyword for the cipher
my_keyword = "friends"

# Encode the message
encrypted_message = vigenere_encode(
    my_message,
    my_keyword
)

print("Encrypted:")
print(encrypted_message)

# Use our decoder from Task 5 to check our work

decoded_again = vigenere_decode(
    encrypted_message,
    my_keyword
)

print("Decoded:")
print(decoded_again)


caesar_decode(message, offset)
caesar_encode(message, offset)

vigenere_decode(message, keyword)
vigenere_encode(message, keyword)

# Come back to this for further 