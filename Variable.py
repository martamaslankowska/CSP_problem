class Variable:
    count = 0

    def __init__(self, val=0):
        Variable.count += 1
        self.value = Variable.count
        self.color = "#FFFFAA"

    def get_value(self):
        print("Value of this variable is:", self.value)
        return self.value






class Constraint:
    counter = 0 # static, global field

    def __init__(self):
        self.id = Constraint.counter + 1
        Constraint.counter += 1
