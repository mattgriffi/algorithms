"""This program is a simulation of the following problem:

On average, there are 10 students in the computer lab in any given hour. There is 1 printer in
this computer lab. On average, each student will need to use the printer twice, and will need
to print between 1 and 20 pages. The printer has two settings: it can print lower quality
at a rate of 10 pages per minute, or higher quality at a rate of 5 pages per minute.

What is the average waiting time per print task for these two methods?
"""

import random

from data_structures.queue import Queue


def main():

    hour = 60 * 60 # Seconds in an hour
    print_chance = 1/180 # On average, 1 print task per 180 seconds
    min_papers = 1
    max_papers = 20
    print_time = 60 / 5 # Seconds to print 1 paper
    printer = Queue()
    busy = False
    timer = 0
    task_time = 0
    current_task = None
    times = []

    # Run the simulation
    for second in range(hour * 5):

        # Create new print tasks
        if second < hour and random.random() < print_chance:
            papers = random.randint(min_papers, max_papers + 1)
            print("New print task: {} papers".format(papers))
            printer.enqueue((papers, second))

        # If the current task has finished
        if busy and timer > task_time:
            timer = 0
            busy = False
            time_taken = second - current_task[1]
            times.append(time_taken)

        # If we just finished a task, start the next
        if not busy and not printer.isEmpty():
            busy = True
            current_task = printer.dequeue()
            task_time = print_time * current_task[0]
            print("Task finished, time taken: {}".format(task_time))

        # Increment the timer on the current task
        timer += 1

    print("Average time per print task: {}\nTotal time for all prints: {}".format(
            sum(times) / len(times), sum(times)))



if __name__ == "__main__":
    main()
