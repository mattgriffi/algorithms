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

    hour = 60 * 60  # Seconds in an hour
    print_chance = 1/180  # On average, 1 print task per 180 seconds
    print_time = 60 / 10  # Seconds to print 1 paper
    printer = Printer(print_time)

    # Run the simulation
    for second in range(hour * 5):

        # Create new print tasks
        if second < hour and random.random() < print_chance:
            new_task = PrintTask(second)
            print("New print task: {} papers".format(new_task.papers))
            printer.enqueue(new_task)

        printer.tick(second)

    times = printer.time_history

    print("Average time per print task: {}\nTotal time for all prints: {}".format(
            sum(times) / len(times), sum(times)))


class PrintTask:
    def __init__(self, time_stamp):
        self.time = time_stamp
        self.papers = random.randint(1, 20)

    def get_wait_time(self, current_time):
        return current_time - self.time


class Printer(Queue):
    def __init__(self, mode):
        super().__init__()
        self.print_time = mode
        self.current_task = None
        self.time_remaining = 0
        self.time_history = []

    def tick(self, time):
        if self.time_remaining > 0:
            self.time_remaining -= 1

        if self.time_remaining == 0:
            if self.current_task:
                print("Task finished, time taken: {}".format(
                        self.current_task.get_wait_time(time))
                )
                self.time_history.append(self.current_task.get_wait_time(time))
            self.start_next_task()

    def start_next_task(self):
        self.current_task = self.dequeue() if not self.isEmpty() else None
        self.time_remaining = self.current_task.papers * self.print_time if self.current_task else 0


if __name__ == "__main__":
    main()
