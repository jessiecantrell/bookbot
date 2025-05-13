#returns the contents of the book at "filepath"
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

#returns the word count from the provided text
def word_count(text):
    words = text.split()
    return len(words)

#returns the character count of the provided text
def character_count(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

#returns a sorted list of dictionaries containing the character count from an unsorted dictionariy
def sort_characters(char_dict):
    sorted_characters = []
    for key in char_dict:
        if key.isalpha():
            sorted_characters.append({"char": key, "num": char_dict[key]})
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
