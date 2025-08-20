def process_file():
    """
    Reads a file, converts its content to uppercase, and writes it to a new file.
    Includes error handling for file not found and read/write permissions.
    """
    # 1. Ask the user for the name of the input file
    input_filename = input("Please enter the name of the file to read: ")

    try:
        # 2. Check if the file exists by trying to open it
        try:
            with open(input_filename, 'r') as test_file:
                pass  # File exists if we can open it
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' does not exist.")
            
            # Ask user if they want to create the file
            create_file = input("Would you like to create this file? (y/n): ").lower()
            if create_file == 'y':
                # Create the file with sample content
                with open(input_filename, 'w') as new_file:
                    sample_content = """Hello, this is a sample text file.
This file was automatically created for demonstration.
You can edit this file with your own content.
Python file handling is an important skill for developers."""
                    new_file.write(sample_content)
                print(f"File '{input_filename}' created successfully with sample content.")
            else:
                print("Operation cancelled.")
                return

        # 3. Read the content of the file
        with open(input_filename, 'r') as file:
            content = file.read()
            print("\nFile successfully read!")

        # 4. Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # 5. Define the new output filename (without os.path.splitext)
        if '.' in input_filename:
            parts = input_filename.split('.')
            base_name = '.'.join(parts[:-1])
            extension = '.' + parts[-1]
        else:
            base_name = input_filename
            extension = ''
            
        output_filename = f"modified_{base_name}{extension}"

        # 6. Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"Content successfully written to '{output_filename}'.")
            print("The modified file has been created.")
            
        # Show a preview of both files
        print("\n" + "="*50)
        print("ORIGINAL FILE CONTENT:")
        print("="*50)
        print(content[:200] + "..." if len(content) > 200 else content)
        
        print("\n" + "="*50)
        print("MODIFIED FILE CONTENT:")
        print("="*50)
        print(modified_content[:200] + "..." if len(modified_content) > 200 else modified_content)

    except PermissionError:
        print(f"Error: Permission denied to read/write '{input_filename}'.")
    except IOError as e:
        # Catch a more general I/O error
        print(f"An I/O error occurred: {e}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("File Processor Program")
    print("=" * 30)
    process_file()