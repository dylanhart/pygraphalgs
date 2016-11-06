class DisjointSets:
	def __init__(self):
		self.sets = {}

	def add_all(self, items):
		s = DisjointSet()
		for i in items:
			self.sets[i] = s

	def add(self, item, to=None):
		if to is not None:
			self.sets[item] = self.sets[to]
		else:
			self.sets[item] = DisjointSet()

	def __contains__(self, item):
		return item in self.sets

	def connect(self, a, b):
		self.sets[a].union(self.sets[b])

	def connected(self, a, b):
		return self.sets[a].find() == self.sets[b].find()


class DisjointSet:
	def __init__(self):
		self.parent = self
		self.rank = 0

	def find(self):
		if self != self.parent:
			self.parent = self.parent.find()
		return self.parent

	def union(self, other):
		rs = self.find()
		ro = other.find()
		if rs == ro: return

		if rs.rank < ro.rank:
			rs.parent = ro
		elif ro.rank < rs.rank:
			ro.parent = rs
		else:
			ro.parent = rs
			rs.rank += 1


