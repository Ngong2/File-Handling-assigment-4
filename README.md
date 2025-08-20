File Processor
A simple Python program that reads a text file, converts its content to uppercase, and saves the modified version to a new file.

Features
Reads text files and converts content to uppercase

Handles missing files by offering to create them

Comprehensive error handling for permissions and I/O issues

Shows previews of original and modified content

Preserves file extensions in output filenames

Usage
Run the program and enter a filename when prompted:

bash
python file_processor.py
If the file doesn't exist, you'll be asked if you want to create it with sample content.

Output
The program creates a new file with the prefix "modified_" (e.g., modified_example.txt from example.txt).

Error Handling
File not found errors

Permission denied errors

General I/O exceptions

Other unexpected errors