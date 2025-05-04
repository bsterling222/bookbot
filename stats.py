def word_count(book_text):
    return len(book_text.split())

def char_count(book_text):
    char_list = {}
    lower_book_text = book_text.lower()
    for char in lower_book_text:
        if char in char_list:
            char_list[char] += 1
        else:
            char_list[char] = 1
    return char_list

def report(char_count):
    alpha_dict = {}
    for char, count in char_count.items():
        if char.isalpha():
            alpha_dict[char] = count

    char_dictionaries = []
    for char, count in alpha_dict.items():
        char_dict = {"char": char, "num": count}
        char_dictionaries.append(char_dict)
    
    char_dictionaries.sort(reverse=True, key=lambda item: item["num"])

    return char_dictionaries

def print_report(word_count, char_count, filepath ):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in report(char_count):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")