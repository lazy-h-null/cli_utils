def print_separator():
    """Prints a line of 30 asterisks to the terminal."""
    print("*" * 30)

def print_char_separator(char):
    print(char * 30)

def print_custom_separator(char, length):
    if length <=0:
        print("")
        return
    print(char * length)

def print_labeled_separator(label, char="*", width=30):
    print(label.center(width, char))

def print_box(message, char="*"):
    width = len(message) + 4
    print(char * width)
    print(char + " " + message + " " + char)
    print(char * width)