#  This is the file which include the clock class used for all remaining upcoming blocks of logic
class clock:
    def __init__(self):
        self.state = 0
        self.tally = 0

    def tick(self):
        self.state = 1 - self.state
        self.tally += 1

    def reset(self):
        self.state = 0
        self.tally = 0
    