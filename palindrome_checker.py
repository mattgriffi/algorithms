"""This program determines whether or not a given string is a palindrome. It uses a Deque,
which is significantly less efficient than just iterating over the string from both ends."""


from data_structures.deque import Deque


class PalindromeChecker:

    @staticmethod
    def check(s):
        deque = Deque()
        # Put each character in the deque (addRear is faster than addFront)
        for c in s:
            deque.addRear(c)
        # Match the front and rear chars in the deque. If we're left with 1 char, it was the
        # middle char and in an odd-length string and can be ignored
        while deque.size() > 1:
            if deque.removeFront() != deque.removeRear():
                return False
        return True
