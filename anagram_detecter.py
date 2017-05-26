"""This program detects whether the given string is an anagram of another given string"""


import time


def main():
    a = "klahsfdkljhasfpiouweafoihdsfa;jskl;sfjapoweiuaypofsafhsjkfhskjfnasfhjpwiureasf"*50
    b = "".join(sorted(a))
    c = b[:-1] + "5"
    result_format = "Algorithm: {}\nCorrect answer: {}\nDerived answer: {}\nTime taken: {:.15f}\n"
    print(result_format.format("Slow", True, *anagram_solver(a, b)))
    print(result_format.format("Slow", False, *anagram_solver(a, c)))

    print(result_format.format("Fast", True, *better_solver(a, b)))
    print(result_format.format("Fast", False, *better_solver(a, c)))


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
    start = time.time()
    if set(a) != set(b):
        return False, time.time() - start
    for c in a:
        if a.count(c) != b.count(c):
            return False, time.time() - start
    return True, time.time() - start


if __name__ == "__main__":
    main()
