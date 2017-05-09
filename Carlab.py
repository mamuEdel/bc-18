class Car(object):
    """docstring for Car"""
    def __init__(self, name=None, model=None, typ=None):
        # default speed of a parked car
        self.speed = 0

        # default name is General, unless otherwise
        if name is None:
            self.name = 'General'
            self.num_of_doors = 4
        else:
            self.name = name

        # default model is GM, unless otherwise
        if model is None:
            self.model = 'GM'
        else:
            self.model = model

        # default type is saloon, unless otherwise
        if typ is None:
            self.typ = 'saloon'
        else:
            self.typ = typ

        # trailer has 8 wheels saloon has 4 wheels
        if typ == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

        # Porsche & Koennigsegg = 2 doors, default = 4 doors
        if name is not None and (name == 'Porshe' or name == 'Koenigsegg'):
            self.num_of_doors = 2
        elif name is not None and (name != 'Porshe' or name != 'Koenigsegg'):
            self.num_of_doors = 4
        else:
            pass

    def is_saloon(self):
        # Return true if type is a saloon
        if self.typ == 'saloon':
            return True
        else:
            return False

    def drive(self, velocity):
        assert isinstance(velocity, int), "Drive argument must be integer"
        # trailer speed
        if self.typ == 'trailer':
            self.speed = velocity * 11
            return self
        # saloon speed
        elif self.typ == 'saloon':
            self.speed = 10 ** velocity
            return self
        else:
pass