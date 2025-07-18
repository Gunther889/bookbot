import sys
from stats import get_book_word_num, get_character_amount, sort_dict, print_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open(path) as f:
        file_content = f.read()
    return file_content

def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    num_words = get_book_word_num(book_text)
    char_num_dict = get_character_amount(book_text)
    sorted_list = sort_dict(char_num_dict)

    print_report(path, num_words, sorted_list)

main()
