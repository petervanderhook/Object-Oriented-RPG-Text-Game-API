class AsciiMap:
	"""map printing and computing"""
	#constructor that takes number of tiles(boxes) and file name
	def __init__(self, tile_divisor, file_name = "./src/asciimap.txt"):
		self.file_name = file_name
		self.tile_divisor = tile_divisor
		#uses encoding to read special characters
		f = open(file_name, encoding = "utf-8")
		text = f.read()
		self.line_list = text.split('\n')
	#method that prints map
	def __repr__(self):
		for line in self.line_list:
			#uses str to print special characters
			print(str(line))
		#keeps __repr__ from getting angie, needs to be fed
		return ""