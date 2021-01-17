class Man:
	def __init__(self, name):
		self.name = name;
		print("Initialized!")

	def hello(self):
		print("Hello,", self.name, "!")

	def bye(self):
		print("bye", self.name, ".")

m = Man("Jeongeun")
m.hello()
m.bye() 
