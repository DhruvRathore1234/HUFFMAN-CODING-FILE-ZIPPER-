import sys

from huffman import Huffman_Coding

path = "sample.txt"

h = Huffman_Coding(path)

output_path = h.compress()

print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)

print("Decompressed file path: " + decom_path)