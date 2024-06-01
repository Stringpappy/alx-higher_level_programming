def write_file(filename="", text=""):
    """ Open the file in write mode with UTF-8 encoding """
    with open(filename, "w", encoding="utf-8") as file:
        # Write the text to the file
        file.write(text)
        return len(text)
