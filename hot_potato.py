"""This program uses a Queue to simulate the children's game of hot potato. The name at the
front of the queue represents the child who is currently holding the potato. """


from data_structures.queue import Queue


def main():
    children = ["Bill","David","Susan","Jane","Kent","Brad"]
    num_turns = 7
    q = Queue()

    while len(children) > 1:

        # Put all the little kiddies in the queue
        for child in children:
            q.enqueue(child)

        # Take turns "passing the potato"
        for turns in range(num_turns):
            q.enqueue(q.dequeue())

        # Off the kid left holding it at the end
        q.dequeue()

        # Put the survivors into a new list
        children = []
        while not q.isEmpty():
            children.append(q.dequeue())

    print("The winner is: {}".format(children[0]))


if __name__ == "__main__":
    main()
