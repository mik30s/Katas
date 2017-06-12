class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children


def post_order(tree):
"""
Performs a post order traversal of a graph
[p] -> [l] -> [r]
"""
	if tree != None:
		# print parent value
		print(tree.val)
		# then print children values
		for sub_tree in tree.children:
			post_order(sub_tree)


def pre_order(tree):
"""
Performs a post order traversal of a graph
[p] -> [l] -> [r]
"""
	if tree != None:
		# then print children values
		for sub_tree in tree.children:
			pre_order(sub_tree.val)
		print(tree)


def in_order(tree):
"""
Performs a post order traversal of a graph
[p] -> [l] -> [r]
"""
	if tree != None and len(tree.children) < 3:
		in_order(tree.children[0]) # traverse left child
		print(tree.val)
		in_order(tree.children[1])


tree = Node(val=2, children=[
			Node(1, children=None),
			Node(3, children=None)
	])





