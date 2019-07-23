class Population:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.num = Property(name+':num')


class Projection:
    def __init__(self, origin, termination):
        self.origin = origin
        self.termination = termination
        self.hit_rate_peak = Property('{}-{}:hrp'.format(origin.name, termination.name)) #fraction -- could be derived from FLNe and in-degree
        self.hit_rate_width = Property('{}-{}:hrw'.format(origin.name, termination.name)) #mm


class Property:
    def __init__(self, name):
        self.name = name
        self.constraints = []

    def get_value(self):
        pass


class Variable:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def get_value(self):
        pass


class Constraint:
    def __init__(self, value, uncertainty, rationale, references, expression=None):
        """
        :param value: A number
        :param uncertainty: Uncertainty of the number; standard deviation of estimated
            probability density
        :param rationale: A short paragraph that describes how the value and uncertainty were
            estimated from data
        :param references: List of references. Each reference is the string identifier of a
            paper that appears in the .bib file, e.g. 'Sincich2002'
        :param expression: Optionally, the constraint can be the result of an expression that
            includes the value as well as Variables, Properties, and literal numbers. The value
            should be referenced with the string 'x' and Variables and Properties should be
            referenced by name.
        """
        pass


class Network:
    def __init__(self):
        self.Populations = []
        self.Projection = []
        self.Variables = []
        self.Constraints = []

    def add_population(self, name, parent=None):
        self.Populations.append(Population(name, parent=parent))

    def get_variable(self, name):
        pass

    def get_property(self, name):
        pass
