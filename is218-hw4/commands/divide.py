class Divide:
    name = "divide"

    def execute(self, a, b):
        a = float(a)
        b = float(b)
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b