class Counter:
    def __init__(self):
        self.turn_count = 0

    def next_turn(self):
        self.turn_count += 1
        return self.turn_count