#!/usr/bin/python3
def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize a list to store lines
    lines = []

    # Initialize a variable to keep track of the current line
    current_line = ""

    # Iterate through each character in the text
    for char in text:
        # Check if the character is one of the specified characters
        if char in ".?:":
            # Add the current line to the list
            lines.append(current_line.strip())

            # Start a new line after the specified character
            current_line = ""
        else:
            # Add the character to the current line
            current_line += char

    # Add the last line to the list
    lines.append(current_line.strip())

    # Print the lines with 2 new lines after each line
    for line in lines:
        print(line)
        print()
