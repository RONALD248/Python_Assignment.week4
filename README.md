# File Read & Write Challenge 🖋️ + Error Handling Lab 🧪

## Overview
This Python program demonstrates how to **read a file**, **modify its contents**, and **write the result into a new file**, while also handling possible errors gracefully.  
It’s designed as part of a learning exercise for mastering **file operations** and **exception handling** in Python.

---

## Features
- 📂 Reads content from a user-specified file.  
- ✍️ Writes modified content into a new file named `output_<filename>`.  
- 🔠 Example modification: Converts all text to **uppercase**.  
- ⚠️ Handles common errors such as:
  - `FileNotFoundError` → If the file does not exist.  
  - `PermissionError` → If the file cannot be accessed.  
  - General exceptions → Any other unexpected issues.  

---

## How It Works
1. The user is prompted to enter the name of a file to read.  
2. The program opens the file, reads its content, and closes it.  
3. The content is converted to uppercase (you can customize this).  
4. A new file is created with the prefix `output_`, containing the modified content.  
5. Success or error messages are displayed based on the outcome.  

---

## Example Usage
```bash
Enter the filename to read: input.txt
✅ Successfully created 'output_input.txt' with modified content.
````

If the file does not exist:

```bash
Enter the filename to read: missing.txt
❌ Error: The file does not exist. Please check the filename and try again.
```

---

## Code

```python
def process_file():
    try:
        filename = input("Enter the filename to read: ")

        file = open(filename, "r")
        content = file.read()
        file.close()

        modified_content = content.upper()

        new_filename = "output_" + filename
        file = open(new_filename, "w")
        file.write("Modified Content:\n")
        file.write(modified_content)
        file.close()

        print(f"✅ Successfully created '{new_filename}' with modified content.")

    except FileNotFoundError:
        print("❌ Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

process_file()
```

---

## Requirements

* Python 3.x
* A text file (e.g., `input.txt`) in the same directory as the script.

---

## Learning Outcomes 🎉

By using this program, you’ll learn:

* How to **read and write files** in Python.
* How to **modify text content** programmatically.
* How to **handle file-related errors** with exceptions.
* Best practices for writing robust and user-friendly programs.
