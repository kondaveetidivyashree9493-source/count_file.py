
try:
    # Open the file in read mode
    with open("example.txt", "r") as file:
        lines = file.readlines()

    # Initialize counters
    characters = 0
    words = 0
    line_count = 0

    # Count characters, words, and lines
    for line in lines:
        line_count += 1
        words += len(line.split())
        characters += len(line)

    # Print the results
    print("Characters:", characters)
    print("Words:", words)
    print("Lines:", line_count)

except FileNotFoundError:
    print("Error: File not found.")

except IsADirectoryError:
    print("Error: The given path is a directory.")

except OSError:
    print("Error: Unable to read the file.")
