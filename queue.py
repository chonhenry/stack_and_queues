#Implement queue using linked list
class node:
	def __init__(self, value):
		self.value = value
		self.nextnode = None

class queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self): #show the top item
		return self.first

	def enqueue(self, item): #add an item to the stack
		new_item = node(item)
		if(self.length == 0):
			self.first = new_item
			self.last = new_item
		else:
			self.last.nextnode = new_item
			self.last = new_item
		self.length+=1

	def dequeue(self): #remove the top item from the stack
		if(self.length==0):
			return None
		elif(self.length==1):
			self.last = None
		del_item = self.first
		del_value = del_item.value
		self.first = self.first.nextnode
		del del_item
		self.length-=1
		return del_value

	def isempty(self): #check if the stack is empty or not
		return (self.length == 0)

	def __str__(self): #print the queue
		current = self.first
		lst = []
		while(current!=None):
			lst.append(current.value)
			current = current.nextnode
		return str(lst)

q = queue()
for i in range(5):
	q.enqueue(i)
print(q)
q.dequeue()
print(q)





