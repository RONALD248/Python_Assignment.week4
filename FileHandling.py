# File Read & Write Challenge + Error Handling Lab.

def process_file():
    try:
        # Ask user for a filename
        filename = input("Enter the filename to read: ")

        # Open the file for reading
        file = open(filename, "r")
        content = file.read()
        file.close()  # must close manually

        # Modify content (example: convert to uppercase)
        modified_content = content.upper()

        # Create a new file and write modified content
        new_filename = "output_" + filename
        file = open(new_filename, "w")
        file.write("Modified Content:\n")
        file.write(modified_content)
        file.close()  # close after writing

        print(f"Successfully created '{new_filename}' with modified content.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run program
process_file()
