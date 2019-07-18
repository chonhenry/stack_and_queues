class node:
	def __init__(self, value):
		self.value = value
		self.nextnode = None

class stack:
	def __init__(self):
		self.top = None
		self.bottom = None
		self.length = 0

	def peek(self): #show the top item
		return self.top

	def push(self, item): #add an item to the stack
		newitem = node(item)
		if (self.top == None):
			self.top = newitem
			self.bottom = newitem
		else:
			temp = self.top
			self.top = newitem
			self.top.nextnode = temp
		self.length+=1

	def pop(self): #remove the top item from the stack
		if(self.top == None):
			return None
		elif (self.top == self.bottom):
			pop_item = self.top.value
			self.top = None
			self.bottom = None
			self.length-=1
			return pop_item
		else:
			pop_item = self.top.value
			temp = self.top
			self.top = self.top.nextnode
			del temp
			self.length-=1
			return pop_item

	def isempty(self): #check if the stack is empty or not
		return (length == 0)

	def print_stack(self):
		lst = []
		current = self.top
		while(current != None):
			lst.append(current.value)
			current = current.nextnode
		print(lst)

s1 = stack()
s1.print_stack
for i in range(1,5):
	s1.push(i)
	s1.print_stack()

for i in range(1,5):
	s1.pop()
	s1.print_stack()

















