class Human:

	def __init__(self,n,r):
		self.name=n
		self.role=r

	def work(self):
		if self.role=='developer':
			print(self.name, "is Python developer")
		elif self.role=='trainer':
			print(self.name, "is Trainer")

	def speak(self):
		print(self.name,"How are you")

saral=Human("saral kumar","developer")
saral.work()
saral.speak()