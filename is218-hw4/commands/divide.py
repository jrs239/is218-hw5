class Divide:
	name = "divide"

	def execute(self, a, b):
		
		try:
			a = float(a)
			b = float(b)
			if b == 0;
				return "Error: Cannot divide by zero."
			return a/b
		except ValueError:
			return "Error: Invalid input. Please enter two numbers."
