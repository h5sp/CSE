class Ball(object):
    def __init__(self):
        self.bounce = True
        self.throw = True
        self.pop = True
        self.kick = True
        self.roll = True

    def bounce(self):
        self.bounce += times
        if self.bounce > 2:
            self.bounce = 2

    def throw(self):
        self.throw += times
        if self.throw > 5:
            self.throw = 5

    def pop(self):
        self.pop += times
        if self.pop > 1:
            self.pop = 1

    def pop_ball(self):
        print("It popped!!")
        self.pop = False

    def kick(self):
        self.kick += times
        if self.kick > 10:
            self.kick = 10

    def roll(self):
        self.roll += times
        if self.roll > 5:
            self.roll = 5
