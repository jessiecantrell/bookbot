from stats import get_book_text
from stats import word_count
from stats import character_count
from stats import sort_characters
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    count = word_count(get_book_text(sys.argv[1]))
    char_list = sort_characters(character_count(get_book_text(sys.argv[1])))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char in char_list:
        print(char["char"] + ': ' + str(char["num"]))

main()
