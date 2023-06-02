def count_symbols(text):
    symbol_count = 0
    # Iterate each character in the text
    for char in text:
        # Check if the character is not alphanumeric and not a whitespace
        if not char.isalnum() and not char.isspace():
            symbol_count += 1
    return symbol_count

def count_alphabets(text):
    alphabet_count = 0
    # Iterate each character in the text
    for char in text:
        # Check if the character is an alphabet
        if char.isalpha():
            alphabet_count += 1
    return alphabet_count

def count_digits(text):
    digit_count = 0
    # Iterate each character in the text
    for char in text:
        # Check if the character is a digit
        if char.isdigit():
            digit_count += 1
    return digit_count

def count_characters(text):
    # Return the length of the text #It gives the total number of characters
    return len(text)

def count_links(text):
    # Count the occurrences
    link_count = text.count("http://") + text.count("https://")
    return link_count

def count_images(text):
    # Count the occurrences of image file extensions in the text
    image_extensions = [".png", ".jpg", ".jpeg", ".gif"]
    image_count = 0
    # Iterate each extension
    for ext in image_extensions:
        # Count the occurrences of the extension in the text
        image_count += text.count(ext)
    return image_count

def process_resume_file(file_path):
    # Read the contents of the resume file
    with open(file_path, 'r') as file:
        resume_text = file.read()

    # Count various elements in the resume text
    symbols = count_symbols(resume_text)
    alphabets = count_alphabets(resume_text)
    digits = count_digits(resume_text)
    characters = count_characters(resume_text)
    links = count_links(resume_text)
    images = count_images(resume_text)

    # Print the counts
    print("Number of symbols:", symbols)
    print("Number of alphabets:", alphabets)
    print("Number of digits:", digits)
    print("Total number of characters:", characters)
    print("Number of links:", links)
    print("Number of images:", images
