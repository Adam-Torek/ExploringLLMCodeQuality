def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])


def main():
    s = input("Enter a string: ")
    print("Encoded string:", encode_shift(s))
    print("Decoded string:", decode_shift(encode_shift(s)))


if __name__ == "__main__":
    main()