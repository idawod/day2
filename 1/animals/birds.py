class Birds:
	def __init__(self):
		self.members = ['Sparrow', 'Robin', 'Duck']

	def printMembers(self):
		for member in self.members:
			print('\t%s' % member)

