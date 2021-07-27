class Website:
	def first(self):
		print ('first')

		
class Second(Website):
	def sec(self):
	    print('second')

		
class Third(Second):
	def final(self):
	    print ('third')

a=Third()
a.first()

a.sec()
a.final()
