class AsciiMap:
	"""map printing and computing"""
	#constructor that takes dimension list and file name
	def __init__(self, dimensions = [15,15], file_name = "asciimap.txt"):
		self.file_name = file_name
		self.dimensions = dimensions
		#uses encoding to read special characters
		f = open(self.file_name, encoding = "utf-8")
		text = f.read()
		self.line_list = text.split('\n')

	#method that prints map
	def __repr__(self):
		for line in self.line_list:
			#uses str to print special characters
			print(str(line))
		#keeps __repr__ from getting angie, needs to be fed
		return ""

	def tiles(self):
		tile_list = []
		tile_list_index = 0
		for line in self.line_list:
			#makes list inside list
			tile_list.append([])
			count = 0
			tile = ""
			for char in line:
				count += 1
				tile += char
				if (count % round(len(line)/self.dimensions[1])) == 0:
					tile_list[tile_list_index].append(tile)
					tile = ""
			if tile != "":
				tile_list[tile_list_index].append(tile)
			tile_list_index += 1
		self.tile_list = tile_list

	def tile_display(self):
		for i in self.tile_list:
			word = ""
			for tile in i:
				word += tile
				word += "-"
			print(str(word))
