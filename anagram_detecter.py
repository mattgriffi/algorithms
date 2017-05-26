"""This program detects whether the given string is an anagram of another given string"""


def main():
    print(anagram_solver("abc", "cba"))
    print(anagram_solver("level", "velel"))
    print(anagram_solver("dog", "cat"))
    print(anagram_solver("god", "dog"))


def anagram_solver(a, b):
    c = list(b)
    # Iterate over string a
    for ca in a:
        found = False
        # Iterate over string b, comparing char of a to chars in b
        for i, cb in enumerate(c):
            if ca == cb:
                c[i] = None
                found = True
                break
        if not found:
            return False
    return True


if __name__ == "__main__":
    main()
