"""This program determines whether or not a given string is a palindrome. It uses a Deque,
which is significantly less efficient than just iterating over the string from both ends."""


from data_structures.deque import Deque


class PalindromeChecker:

    @staticmethod
    def check(s):
        deque = Deque()
        for c in s:
            deque.addRear(c)
        while not deque.isEmpty():
            if deque.removeFront() != deque.removeRear():
                return False
        return True