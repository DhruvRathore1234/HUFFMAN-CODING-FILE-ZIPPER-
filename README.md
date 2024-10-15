
# File Compression and Decompression Tool (Huffman Coding)

This project presents a **file compression and decompression tool** using the **Huffman coding algorithm**. Developed between **May 2023 - July 2023**, the tool compresses large text files by encoding frequently occurring characters with shorter binary codes, optimizing storage space without losing any information. The tool showcases the efficiency of **Huffman coding** by providing both compression and decompression functionalities.

### Project Highlights
- **Huffman Coding Algorithm**: The tool implements the **Huffman coding** algorithm, a widely used **lossless compression** technique. It reduces the size of a text file by assigning shorter binary codes to more frequent characters and longer codes to less frequent ones.
  
- **Encoding & Decoding**: The tool includes functions to **compress** a file (convert it into a binary format) and then **decompress** the file back to its original form. The encoding and decoding are performed efficiently using a **Huffman tree**.

- **Bit Manipulation**: The project demonstrates an understanding of **bit-level operations**, crucial for compressing data to its smallest possible form during the encoding process.

- **Priority Queue for Optimal Pathfinding**: A **priority queue** is used in building the Huffman tree, ensuring that the most frequent characters are encoded with shorter paths.

- **Binary Tree Construction**: The tool constructs and uses a **binary tree** (Huffman tree) where each leaf node represents a character and its frequency in the input text file. The path from the root to the leaf forms the compressed binary code for each character.

### Key Features
- **Efficient Compression**: Converts a text file into a compressed binary file, significantly reducing file size while retaining all original data.
- **Accurate Decompression**: Accurately reconstructs the original file from the compressed binary data using the same Huffman tree.
- **Advanced Data Structures**: Uses **priority queues** for efficient tree building and **bit manipulation** for optimal encoding and decoding performance.
  
### Technical Details
- **Algorithm Design**: Utilizes the **Huffman Coding Algorithm**, which ensures minimal storage space by compressing frequently used characters more efficiently than less frequent ones.
- **Data Structures**: Implements **priority queues** to manage the frequency of characters, and constructs a **binary tree** (Huffman tree) to generate the encoding scheme for each character.
- **Proficiency in Python**: Demonstrates strong skills in Python, leveraging its libraries to implement advanced algorithms for both compression and decompression.

### How to Use
1. **Clone the Repository**:  
   First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   ```

2. **Run the Huffman Tool**:  
   To perform compression and decompression on the provided sample text file (`sample.txt`), open a terminal and run:
   ```bash
   python3 useHuffman.py
   ```

3. **File Outputs**:  
   The tool will create both compressed and decompressed versions of the `sample.txt` file at the same location.

4. **Custom File Compression**:  
   To compress a different text file, edit the `path` variable in the `useHuffman.py` file to point to your custom file.

### Future Enhancements
- **Enhanced Compression Options**: Future versions could explore supporting additional compression algorithms for comparison with Huffman coding.
- **File Format Support**: Extend the tool to support compression of other file types, such as images and videos.
- **User-Friendly GUI**: Introduce a graphical interface for easier file selection, compression, and decompression.

---
