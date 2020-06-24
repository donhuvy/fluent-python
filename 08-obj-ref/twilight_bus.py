class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            # This is the problem, it's aliasing to the
            # input list. Instead, we should make a copy
            # here with:
            #   self.passengers = list(passengers)
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


if __name__ == '__main__':
    basketball_team = ['Sue', 'Tina', 'Maya', 'Diana', 'Pat']
    bus = TwilightBus(basketball_team)
    bus.drop('Tina')
    bus.drop('Pat')
    assert basketball_team == ['Sue', 'Maya', 'Diana']
