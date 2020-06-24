class HauntedBus:
    """A bus model haunted by ghost passengers"""

    '''
    Function may change any mutable object passed in as a parameter.
    Default value is evaluated when the function is defined (i.e., 
    usually when the module is loaded), and the default values become
    attributes of the function object. If a default value is a mutable
    object and you change it, the change will affect every future call
    of the function.

    We should avoid mutable objects as default value for parameters,
    use None instead.
    '''
    def __init__(self, passengers=[]):
        # Just an aliasing to the input default list
        self.passengers = passengers

    def pick(self, name):
        # This will modify the input default list
        self.passengers.append(name)

    def drop(self, name):
        # This will modify the input default list
        self.passengers.remove(name)


if __name__ == '__main__':
    bus1 = HauntedBus(['Alice', 'Bill'])
    bus1.pick('Charlie')
    bus1.drop('Alice')
    assert bus1.passengers == ['Bill', 'Charlie']

    bus2 = HauntedBus()
    bus2.pick('Carrie')
    assert bus2.passengers == ['Carrie']
    
    bus3 = HauntedBus()
    assert bus3.passengers == ['Carrie']
    bus3.pick('Dave')
    assert bus2.passengers == ['Carrie', 'Dave']
    assert bus2.passengers is bus3.passengers
