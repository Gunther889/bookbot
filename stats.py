def get_book_word_num(book_text):
    num_words = len(book_text.split())
    return num_words

def get_character_amount(book_text):
    words = book_text.split()
    char_num_dict = {}
    for word in words:
        for char in word:
            c = char.lower()
            if c in char_num_dict:
                char_num_dict[c] += 1
            else:
                char_num_dict[c] = 1
    return char_num_dict

def sort_dict(char_num_dict):
    def get_num(items):
        return items["num"]
    
    sorted_list = []
    for char, num in char_num_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(key=get_num, reverse = True)
    return sorted_list

def print_report(path, num_words, sorted_list):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}...")
    print(f"----------- Word Count ----------\nFound {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char = item["char"]
        if char.isalpha():
            print(f"{char}: {item['num']}")
    print("============= END ===============")
