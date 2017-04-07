# Example about Classes from the Squid book (around pg 127)
class Particle(object):
    """ A particle is a constituent unit of the universe.

    Attributes
    ----------
    c: charge in units of [e]
    m: mass in units of [kg]
    r: position in units of [meters], r = x + y + z
    """

    roar = "I am a particle!"

    def __init__(self, charge, mass, position):  # Having charge, mass, and postion, in the __init__ allows us to
        # provide that info when initializing the instance.
        """ Initializes the particle with default values for charge c, mass m, and position r. """
        self.c = charge
        self.m = mass
        self.r = position # {'x': 0, 'y': 0, 'z': 0}
