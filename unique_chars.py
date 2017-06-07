"""This program tests to see if a string contains duplicate characters."""


def main():
    print(check("abcde"))
    print(check("abcdc"))


def check(s):
    """Returns False if string s contains any duplicate characters, else True."""
    bit_flags = 0
    for c in s:
        value = ord(c) - ord('a')
        if bit_flags & (1 << value) > 0:
            return False
        bit_flags |= (1 << value)
    return True


if __name__ == "__main__":
    main()
