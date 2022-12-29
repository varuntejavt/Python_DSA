# Linked Lists - Own Implementation

# Create a class to represent Linked List

# The only info we need to store the Linked List is where it starts (the head node of the list)
# We create another class to represent each node of the linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

	# Adding repr to the class to have a helpful representation of the objects
	def __repr__(self):
		return self.data

class LinkedList:
	def __init__(self, nodes=None):
		self.head = None
		if nodes is not None:
			node = Node(data = nodes.pop(0))
			self.head = node
			for elem in nodes:
				node.next = Node(data = elem)
				node = node.next

	# Adding repr to the class to have a helpful representation of the objects
	def __repr__(self):
		node = self.head
		nodes = []
		while node is not None:
			nodes.append(node.data)
			node = node.next
		nodes.append("None")
		return ' --> '.join(nodes)
