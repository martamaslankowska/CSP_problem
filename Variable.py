class Variable:
    def __init__(self):
        self.value = 0

    def __init__(self, val):
        self.value = val

    def get_value(self):
        print("Value of this variable is:", self.value)
        return self.value




class Constraint:
    counter = 0 # static, global field

    def __init__(self):
        self.id = Constraint.counter + 1
        Constraint.counter += 1
