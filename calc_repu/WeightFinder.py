class WeightFinder(object):
	def __init__(self):
		f = open('user_attr.csv')
		self.lines = f.readlines()[1:]
		self.N = len(self.lines)
		f.close()

	def get_user_weight(self, user_id):
		left = 0
		right = self.N
		while left <= right:
			mid = (left+right)/2
			i = int(self.lines[mid].split(',')[0])
			if i == user_id: return mid, float(self.lines[mid].split(',')[1])
			if i < user_id: left = mid
			else: right = mid
		return None

"""
finder = WeightFinder()
print finder.get_user_weight(2649429)
"""
