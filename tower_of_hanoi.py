"""This program solves the Tower of Hanoi puzzle for a given number of disks.

Information about the puzzle can be found here:
https://en.wikipedia.org/wiki/Tower_of_Hanoi

The number of steps to solve the puzzle is 2^n - 1 where n is the number of disks.
"""


import time


def main():

    num_disks = 3
    start, spare, target = 'A', 'B', 'C'
    print_steps = True

    start_time = time.time()

    tower_of_hanoi(num_disks, start, target, spare, print_steps)

    print(f"\nTime taken: {time.time()-start_time:.10f} seconds")


def tower_of_hanoi(height, start, target, spare, print_steps):
    if height >= 1:

        # Move all disks except the largest to the spare peg
        tower_of_hanoi(height - 1, start, spare, target, print_steps)

        # Move the largest disk to the target peg
        if print_steps:
            print(f"{start} moved to {target}")

        # Move all the disks except for the largest to the target peg
        tower_of_hanoi(height - 1, spare, target, start, print_steps)


if __name__ == "__main__":
    main()
