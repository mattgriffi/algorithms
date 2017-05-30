"""This program uses the turtle module to draw a recursive tree. The trunk and branches of
the tree are brown, while the leaves are green. Branch length, number of branches,
and branch angles are all randomized. Each branch is successively shorter, and the width of
the pen scales exponentially with the length of a branch, ensuring that the trunk is thicker
than the leaves.

This program was originally copy/pasted from this book:
http://interactivepython.org/runestone/static/pythonds/Recursion/pythondsintro-VisualizingRecursion.html#
However, it has since been heavily modified.
"""


import random
import turtle

SHOW_ANIMATION = False
BROWN = (160,82,45)

def main():
    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    turtle.colormode(255)
    t.speed(0)

    if SHOW_ANIMATION:
        tree(100, t)
    else:
        turtle.tracer(0, 0)
        tree(100,t)
        turtle.update()

    turtle.done()


def tree(branch_length, t):
    if branch_length > 5:

        # Scale the pen size with the branch length
        t.pensize(1.035 ** branch_length / 1.5)
        t.down()

        # Make trunks brown and leaves green
        t.color(BROWN)
        if branch_length < 20:
            # Randomize the shade of green for the leaves
            t.color((34,random.randint(100, 170),34))

        # Draw the branch
        t.forward(branch_length)

        # Recursively draw a random number of branches
        for i in range(random.randint(2, 3)):

            # Randomize the angle and relative length of each branch
            angle = random.randint(-60, 60)
            reduction = random.randint(7, 15)

            t.right(angle)
            tree(branch_length - reduction, t)
            t.left(angle)

        t.up()
        t.backward(branch_length)


if __name__ == "__main__":
    main()
