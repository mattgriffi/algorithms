"""This program detects whether the given string is an anagram of another given string"""


import time


def main():
    a = "klahsfdkljhasfpiouweafoihdsfa;jskl;sfjapoweiuaypofsafhsjkfhskjfnasfhjpwiureasf"*50
    b = "".join(sorted(a))
    result_format = "Correct answer: {}\nDerived answer: {}\nTime taken: {:.15f}\n"
    print(result_format.format(True, *anagram_solver("level", "velel")))
    print(result_format.format(False, *anagram_solver("dog", "cat")))
    print(result_format.format(True, *anagram_solver(a, b)))


def anagram_solver(a, b):
    start = time.time()
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
            return False, time.time() - start
    return True, time.time() - start


def better_solver(a, b):
    pass


if __name__ == "__main__":
    main()
