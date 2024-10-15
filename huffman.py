print("Huffman Coding")

import os
import heapq

class Huffman_Coding:

	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

	class HeapNode:

		def __init__(self, char, freq):

			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		""" Defining Comparators less_than and equals """

		def __lt__(self, other):

			return self.freq < other.freq

		def __eq__(self, other):

			if other == None:
				return False
			
			if not isinstance(other, Huffman_Coding.HeapNode):
				return False
			
			return self.freq == other.freq
		

	""" Functions for Compression: """

	def make_frequency_dict(self, text): 
		""" Calculate Frequency and Return """

		frequency = {}
		for character in text:
			if not character in frequency:
				frequency[character] = 0
			frequency[character] += 1

		return frequency

	def make_heap(self, frequency):
		""" Make Priority Queue """
		 
		for key in frequency:
			node = self.HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	def merge_nodes(self):
		""" Built Huffman Codes, Save root node in Heap """

		while len(self.heap) > 1:

			node_1 = heapq.heappop(self.heap)
			node_2 = heapq.heappop(self.heap)

			merged_node = self.HeapNode(None, node_1.freq + node_2.freq)
			merged_node.left = node_1
			merged_node.right = node_2

			heapq.heappush(self.heap, merged_node)

	def make_codes_helper(self, root, current_code):

		if root == None:
			return

		if root.char != None:
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")

	def make_codes(self):
		""" Make Codes for Charecters and Save """

		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)

	def get_encoded_text(self, text):
		""" Replace Charecters with Codes and Return """

		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]

		return encoded_text

	def pad_encoded_text(self, encoded_text):
		""" Pad Encoded Text and Return """

		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"
		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text

		return encoded_text

	def get_byte_array(self, padded_encoded_text):
		""" Conver bits into bytes and Return it as byte array"""

		if len(padded_encoded_text) % 8 != 0:
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))

		return b

	def compress(self):

		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"

		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			frequency = self.make_frequency_dict(text)
			self.make_heap(frequency)
			self.merge_nodes()
			self.make_codes()

			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)

			b = self.get_byte_array(padded_encoded_text)
			output.write(bytes(b))

		print("Compressed")
		return output_path


	""" Functions for Decompression: """

	def remove_padding(self, padded_encoded_text):
		""" Remove Padding and Return """

		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:] 
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text

	def decode_text(self, encoded_text):
		""" Decode and Return """

		current_code = ""
		decoded_text = ""

		for bit in encoded_text:
			current_code += bit
			
			if current_code in self.reverse_mapping:
				character = self.reverse_mapping[current_code]
				decoded_text += character
				current_code = ""

		return decoded_text

	def decompress(self, input_path):

		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + "_decompressed" + ".txt"

		with open(input_path, 'rb') as file, open(output_path, 'w') as output:
			bit_string = ""
			byte = file.read(1)

			while len(byte) > 0:
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)

			encoded_text = self.remove_padding(bit_string)

			decompressed_text = self.decode_text(encoded_text)
			
			output.write(decompressed_text)

		print("Decompressed")
		return output_path
